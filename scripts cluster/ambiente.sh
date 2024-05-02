srun --job-name=mitrabajo --time=4:00:00 --partition=besteffort --qos=besteffort --ntasks=1 --mem=2048 --gres=gpu:1 --pty bash -l

cd /scratch/edison.estramil

git clone https://github.com/stevenE07/tscf.git

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

bash Miniconda3-latest-Linux-x86_64.sh -b -p /scratch/edison.estramil/miniconda3

source miniconda3/bin/activate

pip install ultralytics

cd tscf

python prueba.py