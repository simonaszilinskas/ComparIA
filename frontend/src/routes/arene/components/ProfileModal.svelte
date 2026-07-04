<script lang="ts">
  import { auth } from '$lib/auth.svelte'
  import { Button, Modal, Select } from '$components/dsfr'
  import { api } from '$lib/fastapi-client'
  import { m } from '$lib/i18n/messages'

  const PROFESSIONS = [
    'avocat',
    'magistrat',
    'notaire',
    'commissaire_justice',
    'juriste_entreprise',
    'greffier',
    'etudiant_droit',
    'enseignant_chercheur_droit',
    'autre_professionnel_droit',
    'non_juriste',
    'other'
  ] as const
  const AI_USAGE_FREQUENCIES = ['daily', 'weekly', 'monthly', 'rarely', 'never'] as const
  const GENDERS = ['woman', 'man', 'other', 'prefer_not_to_say'] as const
  const AGE_RANGES = [
    'under_18',
    '18_24',
    '25_34',
    '35_44',
    '45_54',
    '55_64',
    '65_plus'
  ] as const

  let profession = $state('')
  let aiUsageFrequency = $state('')
  let gender = $state('')
  let ageRange = $state('')

  function optionsFor(values: readonly string[], group: string) {
    return values.map((value) => ({
      value,
      label: m[`profile.${group}.options.${value}`]()
    }))
  }

  async function submit() {
    const body: Record<string, string> = {}
    if (profession) body.profession = profession
    if (aiUsageFrequency) body.ai_usage_frequency = aiUsageFrequency
    if (gender) body.gender = gender
    if (ageRange) body.age_range = ageRange

    if (Object.keys(body).length > 0) {
      await api.request<void>('/auth/profile', {
        method: 'PATCH',
        credentials: 'include',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
      })
      if (auth.user) Object.assign(auth.user, body)
    }

    const el = document.getElementById('fr-modal-profile')
    // @ts-expect-error - DSFR is globally available
    if (el) window.dsfr(el).modal.conceal()
  }
</script>

<Modal id="fr-modal-profile" titleId="fr-modal-title-profile" sizeClass="fr-col-md-8 fr-col-lg-6">
  <h2 class="text-xl! mb-2!">{m['profile.title']()}</h2>
  <p class="text-sm! text-grey mb-6!">{m['profile.description']()}</p>

  <div class="gap-4 flex flex-col">
    <Select
      id="profile-profession"
      label={m['profile.profession.label']()}
      bind:selected={profession}
      options={[
        { value: '', label: m['profile.selectPlaceholder']() },
        ...optionsFor(PROFESSIONS, 'profession')
      ]}
    />
    <Select
      id="profile-ai-usage-frequency"
      label={m['profile.aiUsageFrequency.label']()}
      bind:selected={aiUsageFrequency}
      options={[
        { value: '', label: m['profile.selectPlaceholder']() },
        ...optionsFor(AI_USAGE_FREQUENCIES, 'aiUsageFrequency')
      ]}
    />
    <Select
      id="profile-gender"
      label={m['profile.gender.label']()}
      bind:selected={gender}
      options={[
        { value: '', label: m['profile.selectPlaceholder']() },
        ...optionsFor(GENDERS, 'gender')
      ]}
    />
    <Select
      id="profile-age-range"
      label={m['profile.ageRange.label']()}
      bind:selected={ageRange}
      options={[
        { value: '', label: m['profile.selectPlaceholder']() },
        ...optionsFor(AGE_RANGES, 'ageRange')
      ]}
    />
  </div>

  <Button text={m['profile.submit']()} onclick={submit} class="w-full! mt-6! justify-center" />
</Modal>
