Identité visuelle du **CIE, Club Informatique de l'EPO** (École Polytechnique de Ouagadougou). Devise : **« Innovons ensemble ! »**. Elle sert d'abord aux affiches et aux visuels des réseaux sociaux.

## Les quatre principes

1. **Fait main, pas généré.** Chaque affiche doit avoir l'air composée dans Photoshop par quelqu'un du club : aplats francs, vrais détourages, grain, trait de pinceau. Pas de dégradé, de lueur néon, d'objet 3D brillant, de particules ni d'image générée par IA.
2. **Le personnage d'abord, 50/50.** Une affiche sur deux a pour héros un personnage illustré (`AffichePersonnage`), l'autre une vraie photo d'un membre du club (`AffichePhoto`). Le personnage est notre signature.
3. **Bleu et blanc, une étincelle orange.** Le bleu et le blanc viennent du logo, l'orange de l'écran de l'ordinateur du logo.
4. **Une info par niveau.** Titre, puis accroche, puis infos pratiques, puis contact. Si on hésite sur ce qu'il faut lire en premier, l'affiche est ratée.

## Formats

| Format | Taille | Usage |
| --- | --- | --- |
| Post 4:5 | 1080 x 1350 px | Format par défaut (Facebook, Instagram, WhatsApp) |
| Story | 1080 x 1920 px | Statut WhatsApp, story ; titre en `titre-impact-m` |
| Carré | 1080 x 1080 px | Annonces courtes, résultats |
| A3 | 297 x 420 mm, 300 dpi, CMJN | Affichage dans l'école ; multipliez les mesures par 3,25 |

Toutes les mesures de ce système sont données pour 1080 px de large. Gardez `marge-affiche` (64 px) libre sur les quatre bords : seuls le sujet et les fonds peuvent déborder.

## Couleurs

- **Répartition 60/30/10** : 60 % de `fond` (blanc ou `bleu-electrique`), 30 % de `bleu-nuit` et `blanc`, 10 % d'`orange` au plus.
- Une affiche est soit **fond blanc** (thème `clair`, avec `fond-grille-papier`), soit **fond bleu** (thème `bleu`, avec `fond-circuit-bleu`). Alternez d'une publication à l'autre.
- Texte courant en `encre`, jamais en noir pur. Titres en `titre`.
- Sur `orange`, écrivez en `encre`. Jamais de texte blanc sur orange, jamais de texte orange sur `bleu-electrique` ou sur blanc : le contraste est trop faible.
- Aucun dégradé. La profondeur vient de la superposition des calques et des ombres (`ombre-detourage`, `ombre-carte`, `ombre-dure`).

## Typographie

Trois familles libres (licence OFL), fournies dans `fonts/` et sur Google Fonts. Installez-les avant d'ouvrir Photoshop.

- **Anton** (`titre-impact`) : le mot clé, 1 à 3 mots, en capitales.
- **Plus Jakarta Sans** (`titre-large`, `sous-titre`, `accroche`, `texte-affiche`, `etiquette`, `mention`) : tout le reste.
- **Caveat Brush** (`annotation`) : une seule annotation manuscrite par affiche, inclinée, qui chevauche le titre. C'est la touche humaine.

Pas plus de quatre tailles de texte sur une affiche. Rien sous 20 px (`mention`) : l'affiche doit se lire sur un téléphone. Accentuez les capitales (É, À).

## Le personnage

C'est ce qui rend le CIE reconnaissable. Construisez une petite équipe de 3 ou 4 personnages récurrents, inspirés des membres du club (par exemple une développeuse, un bricoleur électronique, une designer), et réutilisez-les d'affiche en affiche.

- **Style** : illustration à plat, contour `encre` de 5 px, deux tons d'ombre seulement, sans dégradé. Carnations réalistes, coiffures et vêtements d'ici.
- **Tenue** : sweat ou chemise en `bleu-electrique` ou `bleu-nuit`, un détail `orange`. Toujours un objet tech en main (ordinateur, téléphone, carte électronique, casque).
- **Pose** : expressive, en mouvement, regard vers le titre ou vers nous. Une main ou un objet peut sortir du cadre ou passer devant le bandeau.
- **Détourage** : contour blanc de 10 px (style de calque, Contour, extérieur) et `ombre-detourage`, comme un autocollant posé sur le fond.
- Dessinez-les vous-mêmes ou faites-les dessiner. Pas de personnage généré par IA.

## La photo

- Vrais membres du club, de préférence sur le campus de l'EPO. Pas de banque d'images.
- Détourage au masque, cheveux compris, sans halo. Pas de contour blanc, seulement `ombre-detourage`.
- Étalonnage sobre : ombres légèrement bleutées, peau naturelle, aucun filtre.

## Fonds et textures

- `fond-circuit-bleu` et `fond-circuit-nuit` : pistes de circuit ton sur ton, pour les affiches bleues.
- `fond-grille-papier` : papier quadrillé, pour les affiches blanches.
- `grain-photoshop` : à poser sur tous les fonds, mode Incrustation, opacité 8 à 12 %. C'est lui qui enlève l'effet numérique lisse.
- `trait-pinceau` (orange, blanc, bleu) : pour souligner le titre.
- Disque plein `bleu-nuit` derrière le sujet pour le détacher du fond.

## Composition

- En-tête (`Logo`) en haut à gauche, pilule d'édition en haut à droite.
- Bloc titre (`TitreAffiche`) dans le tiers haut, aligné à gauche.
- Sujet à droite, de 40 à 55 % de la surface, coupé par le bandeau.
- Infos (`BlocInfo`, liste du programme) à gauche dans le tiers bas.
- `BandeauContact` en pied, toujours.
- Un seul élément d'urgence : `Sticker` ou étiquette orange, pas les deux.

## Iconographie

Icônes Phosphor (phosphoricons.com), graisse Bold, en SVG, couleur `encre` sur orange ou `blanc` sur bleu. Logos des réseaux sociaux : versions officielles en blanc uni. Pas d'emoji sur les affiches, pas d'icône 3D.

## Ton et rédaction

- On tutoie : « Rejoins », « Viens coder », « Apporte ton ordinateur ».
- Phrases courtes, verbes d'action, aucun jargon inutile.
- Dates courtes (« Sam. 18 oct. »), heures « 09h00 à 12h00 ».
- La devise « Innovons ensemble ! » signe chaque affiche, dans le bandeau.

## À éviter

Dégradés · lueurs et néons · objets 3D brillants · visages ou personnages générés par IA · plus de trois couleurs vives · texte blanc sur orange · plus d'une annotation manuscrite · texte collé au bord · logo déformé ou recoloré.
