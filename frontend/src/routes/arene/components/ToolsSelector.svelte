<script lang="ts">
  import { CheckboxGroup } from '$components/dsfr'
  import { api } from '$lib/fastapi-client'
  import { m } from '$lib/i18n/messages'
  import { onMount } from 'svelte'

  interface LegalToolOption {
    id: string
    label: string
    description: string
  }

  let {
    enabledSkills = $bindable([]),
    enabledMcpServers = $bindable([])
  }: {
    enabledSkills: string[]
    enabledMcpServers: string[]
  } = $props()

  let skills = $state<LegalToolOption[]>([])
  let mcpServers = $state<LegalToolOption[]>([])

  onMount(async () => {
    try {
      const data = await api.request<{ skills: LegalToolOption[]; mcp_servers: LegalToolOption[] }>(
        '/arena/legal_tools'
      )
      skills = data.skills
      mcpServers = data.mcp_servers
    } catch (e) {
      console.error('[ToolsSelector] Failed to load legal tools', e)
    }
  })
</script>

{#if skills.length || mcpServers.length}
  <div class="gap-3 md:flex-row flex flex-col">
    {#if skills.length}
      <CheckboxGroup
        id="enabled-skills"
        legend={m['arenaHome.legalTools.skills.legend']()}
        options={skills.map((s) => ({ value: s.id, label: s.label }))}
        bind:value={enabledSkills}
        row
      >
        {#snippet labelSlot({ option })}
          {@const skill = skills.find((s) => s.id === option.value)}
          <span title={skill?.description}>{option.label}</span>
        {/snippet}
      </CheckboxGroup>
    {/if}
    {#if mcpServers.length}
      <CheckboxGroup
        id="enabled-mcp-servers"
        legend={m['arenaHome.legalTools.mcpServers.legend']()}
        options={mcpServers.map((s) => ({ value: s.id, label: s.label }))}
        bind:value={enabledMcpServers}
        row
      >
        {#snippet labelSlot({ option })}
          {@const server = mcpServers.find((s) => s.id === option.value)}
          <span title={server?.description}>{option.label}</span>
        {/snippet}
      </CheckboxGroup>
    {/if}
  </div>
{/if}
