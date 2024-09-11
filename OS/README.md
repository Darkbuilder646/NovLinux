# Docker Configuration

## Instructions

# Volume
Si besoin de creer un volume :
```bash
docker volume create lfs-volume
```

### Construire l'image Docker

Pour construire l'image Docker, utilisez la commande suivante :

```bash
cd docker
docker compose build
docker compose up -d
docker-compose exec lfs /bin/bash
```

# Dans le conteneur Docker
```bash
export LFS=/mnt/lfs
mkdir -pv $LFS/{sources,tools}
chmod -v a+wt $LFS/sources
export PATH=$LFS/tools/bin:$PATH
```
# Arreter le conteneur :
```bash
docker-compose down
```

# Reprendre apres avoir arrete :
```bash
docker-compose up -d
docker-compose exec lfs /bin/bash
```
Et dans le conteneur :
```bash
export LFS=/mnt/lfs
export PATH=$LFS/tools/bin:$PATH
```
### Sauvegarder et restaurer un volume :
Sauvegarde :  
```bash
docker run --rm -v lfs-volume:/mnt/lfs -v $(pwd):/backup alpine tar czvf /backup/lfs-volume-backup.tar.gz -C /mnt lfs
```  
```bash
docker run --rm -v lfs-volume:/mnt/lfs -v $(pwd):/backup alpine tar xzvf /backup/lfs-volume-backup.tar.gz -C /mnt
```
