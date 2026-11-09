# -*- coding: utf-8 -*-
"""页面模板（所有文件平铺在根目录）v7 - 优化首页布局"""

TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__</title>
<meta name="keywords" content="__KEYWORDS__">
<meta name="description" content="__DESCRIPTION__">
<meta name="renderer" content="webkit">
<meta name="applicable-device" content="pc,mobile">
<link rel="canonical" href="__CANONICAL__">
<link rel="stylesheet" href="__CSS__">
</head>
<body data-key="__KEY__">
<header class="topbar">
  <div class="wrap head-main">
    <a class="logo" href="index.html" title="新开传奇网站 - 每日更新传奇开服表">
      <span class="logo-cn">新开传奇</span><span class="logo-en">MIR2 NEW</span>
    </a>
    <div class="head-search">
      <form action="https://www.baidu.com/s" method="get" target="_blank" onsubmit="return chksearch(this)">
        <input type="text" name="q" class="search-input" placeholder="搜索版本 / 攻略 / 开服">
        <button type="submit" class="search-btn">搜索</button>
      </form>
    </div>
  </div>
</header>
<nav class="head-nav" aria-label="主导航">
  <div class="head-nav-inner">
  <a href="index.html" class="home">首页</a>
__NAV__
  </div>
</nav>
<section class="notice wrap">
  <i class="ico-notice">公告</i>
  <div class="notice-list">
    <span>新开传奇网站每日更新最新传奇开服信息，所有版本均可直接访问体验。</span>
    <span>理性游戏，谨防网络诈骗，请勿轻信任何形式的线下交易与充值返利。</span>
  </div>
</section>
__CONTENT__
<footer class="footer">
  <div class="wrap foot-main">
    <div class="foot-col">
      <h4>网站导航</h4>
      <ul>
        <li><a href="index.html">网站首页</a></li>
        <li><a href="xinkai.html">最新开服表</a></li>
        <li><a href="fugu.html">复古版本</a></li>
        <li><a href="heji.html">合击版本</a></li>
        <li><a href="danzhiye.html">单职业传奇</a></li>
        <li><a href="gonglue.html">传奇攻略</a></li>
        <li><a href="ceping.html">版本测评</a></li>
        <li><a href="jiaoliu.html">玩家交流</a></li>
      </ul>
    </div>
    <div class="foot-col">
      <h4>热门标签</h4>
      <div class="foot-tags">
        <a href="xinkai.html">新开传奇</a>
        <a href="fugu.html">1.80复古</a>
        <a href="heji.html">英雄合击</a>
        <a href="danzhiye.html">单职业</a>
        <a href="fugu.html">经典重制</a>
        <a href="danzhiye.html">切割吸血</a>
        <a href="xinkai.html">散人天堂</a>
        <a href="ceping.html">版本测评</a>
      </div>
    </div>
    <div class="foot-col">
      <h4>关于本站</h4>
      <p class="foot-about">新开传奇网站专注于每日更新最新传奇开服信息，涵盖复古、合击、单职业、微变等主流版本。本站内容由资深玩家原创整理，力求信息真实客观。</p>
    </div>
  </div>
  <div class="copyright">
    <p>&copy; <span id="cur-year"></span> 新开传奇网站 版权所有</p>
    <p class="foot-disclaim">本站仅为传奇开服信息平台，所发布内容来源于公开信息整理，不代表任何官方立场。</p>
  </div>
</footer>
<script src="base.js"></script>
</body>
</html>"""


INDEX_BODY = r"""
<section class="wrap focus">
  <div class="focus-main">
    <div class="focus-list" id="focusList">
__FOCUS_SLIDES__
    </div>
    <div class="focus-dots" id="focusDots"></div>
  </div>
  <div class="focus-side">
    <div class="block">
      <div class="block-hd"><h2>今日开服时间</h2></div>
      <div class="block-bd">
        <table class="kf-table">
          <thead><tr><th>时间</th><th>版本名称</th><th>类型</th></tr></thead>
          <tbody>
__KF_ROWS__
          </tbody>
        </table>
      </div>
    </div>
  </div>
</section>

<section class="wrap">
  <div class="block">
    <div class="block-hd"><h2><a href="xinkai.html">今日开服一览</a></h2><a class="more" href="xinkai.html">&raquo;</a></div>
    <div class="block-bd">
      <ul class="kaifu-list">
__KAIFU_LIST__
      </ul>
    </div>
  </div>
</section>

<section class="wrap lay-main">
  <div class="col-left">
    <div class="block">
      <div class="block-hd"><h2><a href="xinkai.html">最新资讯</a></h2><a class="more" href="xinkai.html">&raquo;</a></div>
      <div class="block-bd">
        <ul class="list-news big">
__INDEX_NEWS__
        </ul>
      </div>
    </div>
__INDEX_CAT_BLOCKS__
  </div>
  <div class="col-right">
    <div class="block">
      <div class="block-hd"><h2>开服人气榜</h2></div>
      <div class="block-bd">
        <ul class="rank-list">
__RANK_ITEMS_RIGHT__
        </ul>
      </div>
    </div>
    <div class="block">
      <div class="block-hd"><h2>热门标签</h2></div>
      <div class="block-bd foot-tags" style="padding:8px 0">
        <a href="xinkai.html">新开传奇</a>
        <a href="fugu.html">1.80复古</a>
        <a href="heji.html">英雄合击</a>
        <a href="danzhiye.html">单职业</a>
        <a href="fugu.html">经典重制</a>
        <a href="danzhiye.html">切割吸血</a>
        <a href="xinkai.html">散人天堂</a>
        <a href="ceping.html">版本测评</a>
        <a href="gonglue.html">打宝攻略</a>
        <a href="xinkai.html">开服表</a>
        <a href="fugu.html">沉默版本</a>
        <a href="heji.html">连击合击</a>
      </div>
    </div>
    <div class="block">
      <div class="block-hd"><h2>友情链接</h2></div>
      <div class="block-bd">
        <ul class="list-news">
          <li><a href="cp-quming.html">传奇私服网</a></li>
          <li><a href="gl-qidao.html">传奇攻略大全</a></li>
          <li><a href="fg-1-76-huaijiu.html">传奇怀旧版</a></li>
          <li><a href="xk-2026-11-09-1.html">热血传奇开服表</a></li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""


ARTICLE_BODY = r"""
<div class="wrap crumb"><a href="index.html">首页</a> &gt; <a href="__CAT_URL__">__CAT_NAME__</a> &gt; <span>__H1__</span></div>
<section class="wrap lay-main">
  <div class="col-left">
    <div class="article-box">
      <h1>__H1__</h1>
      <div class="article-info">
        <span>栏目：__CAT_NAME__</span>|<span>发布时间：__DATE__</span>|<span>阅读：__READ__</span>|<span>来源：新开传奇网站</span>
      </div>
      <div class="article-content">
__CONTENT__
        <h2>相关阅读推荐</h2>
        <p>关于__CAT_NAME__，玩家还可以延伸阅读以下文章：__RELATED_LINKS__。想了解更多__CAT_NAME__内容，欢迎浏览本站对应栏目，持续更新中。</p>
      </div>
      <div class="art-tags">本文标签：__TAGS__</div>
    </div>
    <div class="pager" style="margin:16px 0">
      <a href="index.html">返回首页</a>
      <a href="__CAT_URL__">返回栏目</a>
      __NEXT_LINK__
    </div>
    <div class="art-rel">
      <h4>相关文章推荐</h4>
      <ul>
__RELATED_ITEMS__
      </ul>
    </div>
  </div>
  <div class="col-right">
    <div class="block">
      <div class="block-hd"><h2>热门文章</h2></div>
      <div class="block-bd">
        <ul class="list-news">
__HOT_ITEMS__
        </ul>
      </div>
    </div>
    <div class="block">
      <div class="block-hd"><h2>最新开服</h2></div>
      <div class="block-bd">
        <ul class="list-news">
__LATEST_ITEMS__
        </ul>
      </div>
    </div>
    <div class="block">
      <div class="block-hd"><h2>浏览排行</h2></div>
      <div class="block-bd">
        <ul class="rank-list">
__VIEW_RANK__
        </ul>
      </div>
    </div>
  </div>
</section>
"""


CATEGORY_BODY = r"""
<div class="wrap crumb"><a href="index.html">首页</a> &gt; <span>__CAT_NAME__</span></div>
<section class="wrap">
  <div class="cat-hd">
    <h1>__CAT_NAME__<small>共 __COUNT__ 篇文章</small></h1>
    <p>__CAT_DESC__</p>
  </div>
</section>
<section class="wrap lay-main">
  <div class="col-left">
    <div class="block">
      <div class="block-hd"><h2>最新文章</h2><a class="more" href="index.html">&raquo;</a></div>
      <div class="block-bd">
        <ul class="list-news big">
__CAT_ITEMS__
        </ul>
      </div>
    </div>
  </div>
  <div class="col-right">
    <div class="block">
      <div class="block-hd"><h2>栏目导航</h2></div>
      <div class="block-bd">
        <ul class="list-news">
__CAT_NAV__
        </ul>
      </div>
    </div>
    <div class="block">
      <div class="block-hd"><h2>热门文章</h2></div>
      <div class="block-bd">
        <ul class="list-news">
__HOT_ITEMS__
        </ul>
      </div>
    </div>
  </div>
</section>
"""


NAV_ITEMS = [
    ("xinkai", "最新开服"),
    ("fugu", "复古版本"),
    ("heji", "合击版本"),
    ("danzhiye", "单职业"),
    ("gonglue", "传奇攻略"),
    ("ceping", "版本测评"),
    ("jiaoliu", "玩家交流"),
]

CAT_INFO = {
    "xinkai": {"name": "最新开服", "url": "xinkai.html", "desc": "新开传奇网站每日整理最新传奇开服信息，包含开服时间、版本类型、人气热度与入口说明。覆盖复古、合击、单职业、微变等主流版本，方便玩家第一时间找到心仪的服务器。"},
    "fugu": {"name": "复古版本", "url": "fugu.html", "desc": "新开传奇网站汇集1.76、1.80等经典复古传奇版本的开服信息与版本测评。复古服节奏慢、装备保值、社区友好，适合怀旧老玩家和长期养老，每日更新最新开服。"},
    "heji": {"name": "合击版本", "url": "heji.html", "desc": "新开传奇网站提供英雄合击版本的开服信息、职业搭配攻略和PK技巧。合击版本注重操作和团队配合，主副英雄组合策略丰富，适合喜欢竞技的玩家。"},
    "danzhiye": {"name": "单职业", "url": "danzhiye.html", "desc": "新开传奇网站提供单职业传奇版本的开服信息与玩法攻略。单职业版本门槛低、节奏适中、散人友好，适合新手和休闲玩家，切割系统让成长更有爽感。"},
    "gonglue": {"name": "传奇攻略", "url": "gonglue.html", "desc": "新开传奇网站提供传奇各职业练级、技能加点、装备强化、打宝地图等全面攻略，帮助玩家快速上手游戏。涵盖战士、法师、道士三职业的核心技巧。"},
    "ceping": {"name": "版本测评", "url": "ceping.html", "desc": "新开传奇网站从爆率、人气、氪金度、散人友好度等多个维度对各类传奇版本进行客观测评，帮助玩家选择适合自己的服务器。内容由资深玩家原创整理。"},
    "jiaoliu": {"name": "玩家交流", "url": "jiaoliu.html", "desc": "新开传奇网站为传奇玩家提供交流平台，分享游戏故事、行会经验、攻城战报。重温那些年一起传奇的热血岁月，与志同道合的玩家一起探讨游戏乐趣。"},
}
