= ApIssitant =

== ROCM ==
https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/native_linux/install-radeon.html

wget https://repo.radeon.com/amdgpu-install/6.3.4/ubuntu/noble/amdgpu-install_6.3.60304-1_all.deb
apt install ./amdgpu-install_6.3.60304-1_all.deb 
amdgpu-install -y --usecase=graphics,rocm,rocmdev
usermod -a -G video,render
apt install python3-virtualenv

== Deepseek ==
https://docs.openwebui.com/tutorials/integrations/deepseekr1-dynamic/

virtualenv apissistant
source bin/activate
git clone https://github.com/ggml-org/llama.cpp

cmake -B build -DGGML_BLAS=OFF -DCMAKE_INSTALL_PREFIX=/data/

cmake --build build --config Release -j 12
cmake --install build

pip install huggingface_hub hf_transfer
pip install huggingface_hub[hf_xet]

./apissistant/localdeepseekdl.py

