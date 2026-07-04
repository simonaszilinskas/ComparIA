from pydantic import BaseModel


class Skill(BaseModel):
    id: str
    label: str
    description: str
    prompt_content: str


AVAILABLE_SKILLS: dict[str, Skill] = {
    "privacy_policy_analysis": Skill(
        id="privacy_policy_analysis",
        label="Analyse de politique de confidentialité",
        description=(
            "Structure la réponse comme une analyse RGPD : finalités du traitement, "
            "base légale, données collectées, durées de conservation, transferts hors "
            "UE, droits des personnes concernées, et points de vigilance."
        ),
        prompt_content=(
            "Quand l'utilisateur te soumet ou te questionne sur une politique de "
            "confidentialité ou un traitement de données personnelles, structure ta "
            "réponse en sections claires : (1) finalités du traitement, (2) base "
            "légale invoquée (art. 6 RGPD), (3) données collectées et durées de "
            "conservation, (4) transferts hors Union européenne le cas échéant, "
            "(5) droits des personnes concernées (accès, rectification, effacement, "
            "opposition), (6) points de vigilance ou clauses ambiguës/à risque. "
            "Cite les articles du RGPD pertinents. Précise que ton analyse est une "
            "aide à la lecture et ne remplace pas un avis juridique."
        ),
    ),
}
