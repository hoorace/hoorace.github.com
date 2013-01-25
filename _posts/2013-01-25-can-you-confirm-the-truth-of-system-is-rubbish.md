---
comments: true
date: 2013-01-25 11:52:19
layout: post
slug: can-you-confirm-the-truth-of-system-is-rubbish
title: 系统很垃圾，你能证明么？
categories:
- review
tag:
- jenkins
- sonar
- findbugs
- checkstyle

---

&nbsp;&nbsp;&nbsp;&nbsp;最近一个月公司某部门把系统的问题整理成execl不断的反馈给技术部，这些问题有些是用户发现的，有些是他们自己发现的，有些需求是他们自己谈论的。问题和需求汇聚成册，给到技术部，然后技术部清楚的知道：资源应该向什么地方倾斜一下。如果用打仗来比喻创业，他们清楚的告诉后方，在9点钟方向，距离我2000M的地方发现敌情，迅速的炮火支援。然后我只需要把炮弹准确的击中目标就好了。<br />

&nbsp;&nbsp;&nbsp;&nbsp;“文人相轻”的现象尤其在程序员圈子中表现的明显。我相信不少程序开发团队中，都会存在说系统代码很烂的人，如果你让他们说出50条的理由，他们又说不出来，说别人差劲的人往往自己也不怎么样！“相轻”的行为，需要有各种装逼的利器，如果本身素质不能达到一定的水平，就尴尬了。<br />

 <p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp;case : 程序员 
</strong></span></p><div style="border-left: 2px solid rgb(204, 204, 204); padding-left: 6px; margin-left: 6px; margin-bottom: 10px;">

&nbsp;&nbsp;&nbsp;&nbsp;反馈系统问题当然需要具体的证据，程序员想证明您的同事写的代码一般般，必须拿数据说话。“工欲善其事，必先利其器”，所以找到各种利器是你的不二法宝，随手搭建一个[Jenkins](http://jenkins-ci.org/) + [Sonar](http://www.sonarsource.org/)的系统，导入你们的代码，然后搞个PPT show给你的同事们，让他们当场脸红。您至少可以列出以下事实：<br />

* 代码注释率，有没有30%？
* 测试代码覆盖率有多少？
* 重复代码量，是否高于5%？
* 哪些地方的代码需要重构，可以一一列出；
* 通过timemachine看看复杂度，覆盖率，方法复杂度的变化。给出你的建议
* ……剩下的就是自己去研究sonar

&nbsp;&nbsp;&nbsp;&nbsp;或者您可以懒惰一点，给IDE安装一个[findbugs](http://findbugs.sourceforge.net/index.html)去找出系统中的100个问题，如果您觉得想找出更多问题，可以考虑给您的IDE安装一个[checkstyle](http://checkstyle.sourceforge.net/)，列出200个系统问题。当然没有前面的方法酷而已。<br />
&nbsp;&nbsp;&nbsp;&nbsp;当然如果你是真正的高手，你需要教一下我在不适用任何工具的情况下，最快的速度把代码中的问题查找出来。查找代码的问题只是小Case，能够通过代码看出系统架构设计的问题才是牛人。例如：日志的规范化，测试的框架化，核心系统plugin的构建，框架的深入使用，服务的抽离…… <br />
&nbsp;&nbsp;&nbsp;&nbsp;这个一个没有止境的工作，所以没事只需要行动，不要说话。
 </div>
 <p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp;case : 产品经理
</strong></span></p><div style="border-left: 2px solid rgb(204, 204, 204); padding-left: 6px; margin-left: 6px; margin-bottom: 10px;">
&nbsp;&nbsp;&nbsp;&nbsp;能够说出[okhqb.com](http://www.okhqb.com)网站的会员营销的产品的50个改进细节的人，您就不要过来凑热闹了，我写的内容对您没有帮助。因为，我只是兼职的搞过产品，说下自己的心得而已。<br />
&nbsp;&nbsp;&nbsp;&nbsp;互联网的产品，需要价值驱动。能够形成产品闭环才能创造价值。例如：用户营销方面，第一步用户注册，应该如何诱惑；第二步用户购买应该如何驱动；第三步如何让用户的朋友也过来买；第四步买完商品后给用户什么样的好处。让用户在第二步和第四步不断循环，创造出指数的价值。<br />
&nbsp;&nbsp;&nbsp;&nbsp;你的系统烂，是不是没有形成闭环，是不是没有指数级的产品，而这些点到面的寻找可以帮助公司和自己成长。而简单的说产品做的差，没有价值。<br />
&nbsp;&nbsp;&nbsp;&nbsp;我理解的产品，一个需要用户价值驱动，一个数据驱动，二者有效的结合起来带来更大的价值，或者说否则是前者优化的驱动力。<br />
 </div>
 <p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp; case : 用户服务 
</strong></span></p><div style="border-left: 2px solid rgb(204, 204, 204); padding-left: 6px; margin-left: 6px; margin-bottom: 10px;">
&nbsp;&nbsp;&nbsp;&nbsp;提到用户最近的，当然是客服人员和销售人员。如果一个程序员去当了客服或者是销售，就能很好的连接到开发端和服务端。例如给我们提交需求的人以前就是一枚程序员，他知道如何和开发人员打交道。<br />
&nbsp;&nbsp;&nbsp;&nbsp;所谓的 [Connect The Dots ](http://v.youku.com/v_show/id_XMTM3OTM5OTA0.html)或许说的就是人应该拥有多重技能去更好的工作，你会发现得诺贝尔奖的不少是在边缘科技上串起来的人（这个是我同学告诉我的，我认为是存在的）。而工作中也需要有这样的角色。有时候在新的领域的努力只需要20%而却能收获80%的成果，或许，这就是所谓的连接点的价值。
 </div>
&nbsp;&nbsp;&nbsp;&nbsp;古人总结一句话叫：“严于律己，宽厚待人”。“满瓶子不荡半瓶子荡”的情况处处都是存在的，批评别人的时候需要小心，您真的是高手么？请拿出证据！
