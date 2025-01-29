# download variable stats and checkpoints from our bucket, see README for original source

set -e
mkdir -p data/stats
mkdir -p checkpoints
gsutil -m cp -r gs://borealis-models/fourcastnet/stats/* data/stats/
gsutil -m cp -r gs://borealis-models/fourcastnet/checkpoints/* checkpoints/