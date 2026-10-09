# Vidéo de présentation du CIE

Animation de 49 secondes au format vertical (1080 x 1920, 30 images par seconde), entièrement en HTML et calée temps par temps sur la musique.

## Le fil de la vidéo

Un curseur orange sert de fil rouge et passe d'une scène à l'autre :

1. « > bonjour le monde » s'écrit, puis « Ici, on code, on partage, on apprend ».
2. Chargement de l'esprit CIE (la barre se fige pendant le silence, puis repart).
3. Drop : le logo et les lettres C, I, E.
4. « Des jeunes passionnés d'informatique et de partage », avec les accolades qui s'ouvrent.
5. Les activités en photos autocollantes : formations, ateliers, Code Battle, remises de prix.
6. `si (débutant || expert) { bienvenue(); }` puis « Tout le monde est bienvenu ».
7. « On invite des experts et nos membres partagent », montage photo, « Ensemble ».
8. Carte de fin : logo, « Innovons ensemble ! », « Rejoins le club ».

## Ce qui n'est pas dans le dépôt

Les photos des membres et la musique ne sont pas publiées ici (dépôt public). Pour refaire le rendu, ajoutez dans `motion/assets/` :

- `p_formation.jpg`, `p_atelier.jpg`, `p_codebattle.jpg`, `p_prix.jpg` : photos 800 x 1000 pour les cartes autocollantes ;
- `f_prix.jpg`, `f_cadeaux.jpg`, `f_attestation.jpg`, `f_atelier.jpg`, `f_formation.jpg`, `f_codebattle.jpg` : photos 1080 x 1920 pour le montage ;
- la musique sous le nom `musique.mp3`.

## Calage sur la musique

Tout est réglé en haut du script de `index.html` :

- `P = 0.4686144` : durée d'un temps (128 BPM) ;
- `SYNC = -0.01` : l'image arrive 10 ms avant le son ;
- `DUR = 49.2` : durée totale.

L'extrait commence à **93,656 s** du morceau : 24 temps calmes, le drop au temps 24, 64 temps de refrain, puis la fin du morceau. Pour un autre morceau, changez `P`, l'instant de départ et, si besoin, les numéros de temps de chaque scène dans `render(t)`.

## Faire le rendu

```bash
cd motion
pip install playwright
python3 render.py 0 1            # écrit frames/00000.jpg ... (1476 images)

ffmpeg -ss 93.656 -t 49.2 -i musique.mp3 -af "afade=t=in:d=0.12,afade=t=out:st=48.5:d=0.7" son.wav
ffmpeg -framerate 30 -i frames/%05d.jpg -i son.wav -c:v libx264 -crf 20 -pix_fmt yuv420p \
       -c:a aac -b:a 160k -shortest -movflags +faststart CIE-motion.mp4
```

Pour aller plus vite, lancez plusieurs rendus en parallèle : `python3 render.py 0 2` et `python3 render.py 1 2`.

`shots.py` sort quelques images à des instants précis pour vérifier une scène : `python3 shots.py 11.3,20.5 test`.
