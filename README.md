# Design CIE

Identité visuelle du **CIE, Club Informatique de l'EPO** (École Polytechnique de Ouagadougou). Devise : **« Innovons ensemble ! »**

Ce dépôt contient trois choses :

| Dossier | Contenu |
| --- | --- |
| [`design-system/`](design-system/) | La charte : couleurs, typographies, textures, logo, éléments d'affiche et gabarits. |
| [`motion/`](motion/) | Le code de la vidéo de présentation du club (motion design calé sur la musique). |
| [`bureau/`](bureau/) | La vidéo de présentation du bureau et l'appel aux candidatures. Les textes se modifient dans `bureau/contenu.json`, la vidéo se refait toute seule dans GitHub Actions. |

## Démarrer vite

- **Lire la charte** : [`design-system/README.md`](design-system/README.md).
- **Faire une affiche dans Photoshop** : installez les polices de `design-system/fonts/`, partez d'un fond de `design-system/assets/Fonds/`, ajoutez `grain-photoshop.png` en Incrustation à 10 %, puis suivez un des deux gabarits (`AffichePersonnage` ou `AffichePhoto`).
- **Utiliser la charte dans un site** : chargez `design-system/tokens.css` puis `design-system/components/bundle.css`.
- **Voir les composants** : ouvrez n'importe quel `design-system/components/*/preview.html` dans un navigateur.

## Couleurs

| Nom | Valeur | Rôle |
| --- | --- | --- |
| `bleu-nuit` | `#122376` | Anneau du logo, blocs sombres |
| `bleu-electrique` | `#2346e0` | Grands fonds, titres sur blanc |
| `bleu-ciel` | `#dfe6ff` | Panneaux sur fond blanc |
| `orange` | `#ee7e1e` | L'étincelle (10 % maximum), texte dessus en `encre` |
| `blanc` / `papier` | `#ffffff` / `#f4f6fb` | Fonds clairs |
| `encre` | `#0b1440` | Texte courant, bandeau contact |

## Polices

Anton (titres), Plus Jakarta Sans (texte), Caveat Brush (annotation manuscrite). Toutes sous licence SIL Open Font License, fichiers de licence dans `design-system/fonts/`.
