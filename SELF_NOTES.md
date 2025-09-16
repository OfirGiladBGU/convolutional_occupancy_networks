- Use server with GTX 1080
- then install the following libs:
```
pip install torch==1.7.1+cu101 torchvision==0.8.2+cu101 -f https://download.pytorch.org/whl/torch_stable.html
pip install torch-scatter==2.0.7 -f https://pytorch-geometric.com/whl/torch-1.7.1+cu101.html
```


COMMANDS:

<!-- python generate.py configs/pointcloud_crop/parse.yaml -->
python generate.py configs/pointcloud/parse.yaml