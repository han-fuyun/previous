#### 记录实现用Fast R-CNN来实现太阳射电爆发的目标检测
##### 具体想法：
1.首先用普通的CNN来训练已有的数据，得到一个还不错的效果  
2.用selective search 得到候选框  
3.怎么来训练spp-net  
4.退而求其次，使用R-CNN来得到结果  
5.SPP-Net是用来同时检测大物体和小物体，CNN是提前训练好的，
只有后面的全连接是微调的（好像是）  
6.用已经训练好的VGG-16或VGG-19，后面加一个SPP-Net，进行全连接层的微调训练  
7.时间安排（2021.5.11）：  
周二周三：  
使用selective search，生成候选框，先对R-CNN进行搭建
周五：  
得到R-CNN的训练结果，并进行微调  
周六周日：  
完成SPP-Net的搭建和训练  
下周一周二：完成Fast R-CNN的搭建  
下周三周四：总结所用过的方法，得到一个结果  





