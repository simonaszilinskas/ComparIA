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

  let profession = $state('')

  const professionOptions = PROFESSIONS.map((value) => ({
    value,
    label: m[`profile.profession.options.${value}`]()
  }))

  async function submit() {
    if (profession) {
      await api.request<void>('/auth/profile', {
        method: 'PATCH',
        credentials: 'include',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ profession })
      })
      if (auth.user) auth.user.profession = profession
    }

    const el = document.getElementById('fr-modal-profile')
    // @ts-expect-error - DSFR is globally available
    if (el) window.dsfr(el).modal.conceal()
  }
</script>

<Modal id="fr-modal-profile" titleId="fr-modal-title-profile" sizeClass="fr-col-md-8 fr-col-lg-6">
  <h2 class="text-xl! mb-2!">{m['profile.title']()}</h2>
  <p class="text-sm! text-grey mb-6!">{m['profile.description']()}</p>

  <Select
    id="profile-profession"
    label={m['profile.profession.label']()}
    bind:selected={profession}
    options={[{ value: '', label: m['profile.selectPlaceholder']() }, ...professionOptions]}
  />

  <Button text={m['profile.submit']()} onclick={submit} class="w-full! mt-6! justify-center" />
</Modal>
