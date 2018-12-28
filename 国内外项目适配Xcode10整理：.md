### 国内外项目适配Xcode10整理：

* **UIButton的dh_enable属性找不到**

  解决方法：将UIView + Ex.swift改成OC的分类，分别添加到Bridge+Pch文件中供swift和OC获取分类属性，并将UIButton+Lechange.swift里的dh_enable去除。

* **ld: symbol(s) not found for architecture arm64 **

  解决方法：此方法大概率是因为个别库不支持真机/模拟器的arm64架构。需要更新编译不过的组件库

* **Apple Link O Error......std::…….**

  解决方法: C++的一些方法错误，需要更换C++库。Build Phases ->Link Binary With Libraries, 删除libstdc++.6.0.9.tbd,增加libc++.tbd

