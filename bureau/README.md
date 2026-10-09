# Vidéo du bureau

Présentation des membres du bureau du CIE, puis appel aux candidatures pour le prochain bureau. Format vertical 1080 x 1920, calé temps par temps sur la musique.

**Tu ne touches qu'à un seul fichier : [`contenu.json`](contenu.json).** La vidéo se refait toute seule dans le cloud (GitHub Actions) à chaque modification.

## Modifier les textes

1. Ouvre `bureau/contenu.json` sur GitHub et clique sur le crayon (ça marche aussi sur téléphone).
2. Change le texte **entre guillemets**. Garde les guillemets, les deux-points et les virgules.
3. Clique sur **Commit changes**.
4. Va dans l'onglet **Actions** : la vidéo se fabrique (environ 10 minutes). Quand c'est vert, ouvre le rendu et télécharge **video-bureau** en bas de la page. Tu y trouveras `bureau-cie.mp4` (HD) et `bureau-cie-whatsapp.mp4` (léger).

Si le rendu devient rouge, c'est presque toujours une virgule ou un guillemet oublié dans `contenu.json`. Colle le fichier sur [jsonlint.com](https://jsonlint.com) pour trouver la ligne.

### Un membre

```json
{
  "poste": "Secrétaire",
  "nom": "Prénom Nom",
  "description": "Une ou deux phrases, 90 caractères environ.",
  "photo": "photos/secretaire.jpg",
  "cadrage": "50% 30%",
  "style": ""
}
```

| Champ | À quoi ça sert |
| --- | --- |
| `poste` | Écrit lettre par lettre dans l'étiquette orange. |
| `nom` | Le grand titre. Il se réduit tout seul s'il est long. |
| `description` | Apparaît mot par mot. Elle se réduit si elle est longue, mais reste courte pour qu'on ait le temps de la lire. |
| `photo` | Le chemin de la photo. Vide = silhouette en attendant. |
| `cadrage` | Quelle partie de la photo garder : `"50% 30%"` = centré, plutôt le haut (le visage). `"50% 0%"` remonte, `"50% 60%"` descend. |
| `style` | Vide = automatique. Sinon `"bleu"`, `"papier"`, `"nuit"` ou `"code"` pour forcer la mise en page. |

- **Ajouter un membre** : copie un bloc `{ ... }`, colle-le après un autre et mets une virgule entre les deux. La vidéo s'allonge de 6 secondes par membre.
- **Retirer un membre** : supprime son bloc (et la virgule en trop).
- **Changer l'ordre** : déplace les blocs.

### Les photos

Dépose-les dans `bureau/photos/` (sur GitHub : **Add file**, puis **Upload files**). Format portrait conseillé, au moins 800 x 1000 pixels, visage dans le tiers haut. Écris ensuite leur chemin dans `photo`, par exemple `"photos/president.jpg"`.

### L'intro, les remerciements et l'appel aux candidatures

Tout est dans `contenu.json` : `intro`, `merci` et `appel`. Les mots entre accolades sont remplacés automatiquement :

- `{n}` : le nombre de membres ;
- `{mandat}` : le mandat actuel (`"mandat"`) ;
- `{prochain_mandat}` : le prochain (`"prochain_mandat"`).

Pense à remplacer `"Élections : date à préciser"` par la vraie date dans `appel` > `infos`. Les icônes possibles sont `calendrier`, `lieu`, `contact` et `horloge`.

## La musique

Le rendu cherche `bureau/musique.mp3`. **Elle n'est pas dans le dépôt** : c'est un morceau protégé et le dépôt est public. Deux possibilités :

- passer le dépôt en privé (Settings, puis Danger Zone, puis Change visibility), puis déposer `musique.mp3` dans `bureau/` ;
- ou laisser le rendu cloud muet et ajouter la musique au montage.

Les réglages de calage sont dans `musique` (tempo 82,5 BPM, premier temps à 0,0376 s). Ne les change que si tu changes de morceau.

## Prévisualiser sur ton ordinateur

```bash
cd bureau
python3 -m http.server
```

Puis ouvre <http://localhost:8000> : bouton **Lire** et curseur pour naviguer dans la vidéo, avec le son si `musique.mp3` est présent.

## Faire le rendu sur ton ordinateur

```bash
cd bureau
pip install playwright
python -m playwright install chromium
python3 render.py              # vidéos dans bureau/sortie/
python3 render.py --apercu 12,30,60   # quelques images de contrôle
```

## Déroulé

| Temps (pour 10 membres) | Scène |
| --- | --- |
| 0 à 12 s | Terminal : `ls bureau/` liste les postes, puis « 10 membres. Une seule équipe. » |
| 12 à 17 s | Le titre : logo, LE BUREAU, mandat |
| 17 à 76 s | Un membre toutes les 6 s, quatre mises en page en alternance (bleu, papier, nuit, code) |
| 76 à 79 s | MERCI avec la mosaïque des membres |
| 79 à 85 s | `candidats --bureau 2026-2027` puis « Et toi ? » |
| 85 à 91 s | Candidatures ouvertes, le titre de l'élection et les infos pratiques |
| 91 à 99 s | Carte de fin : logo, devise, « Présente-toi ! » |
