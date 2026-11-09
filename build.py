# -*- coding: utf-8 -*-
"""新开传奇网站 - 静态站点生成器 v7 (优化首页布局)"""
import os
import re
from collections import defaultdict
from data_articles import ARTICLES
from tpl_page import TEMPLATE, INDEX_BODY, ARTICLE_BODY, CATEGORY_BODY, NAV_ITEMS, CAT_INFO

SITE_URL = "https://playercq.github.io"
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ============ 工具函数 ============

def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')

def nav_html(key=""):
    items = []
    for k, name in NAV_ITEMS:
        cls = f' class="{k} active"' if k == key else f' class="{k}"'
        items.append(f'<a href="{CAT_INFO[k]["url"]}"{cls}>{name}</a>')
    return "\n".join(items)

def render_template(tpl, ctx):
    content = ctx.get("__CONTENT__", "")
    result = tpl
    for key, val in ctx.items():
        if key != "__CONTENT__":
            result = result.replace(key, str(val))
    if content:
        result = result.replace("__CONTENT__", str(content))
    return result

# ============ 首页生成 ============

def build_index(articles_by_cat):
    focus_arts = [
        ("p1", "最新开服", "xk-2026-11-09-1", "11月9日最新开服时间表公布", "今天共有8个新区开放，覆盖复古、合击、单职业、微变四大类版本。"),
        ("p2", "合击版本", "hj-heji-zuhe", "英雄合击最强组合实测排名", "从打宝、PK、团战三个维度实测英雄合击各职业组合。"),
        ("p3", "单职业", "dz-weihe-huanying", "单职业传奇为什么越来越受欢迎", "从玩法简化、节奏适中、社交友好三个维度分析。"),
        ("p4", "复古版本", "fg-1-80-yuanban", "1.80复古传奇为什么至今仍有人玩", "从怀旧情怀、玩法深度、社交氛围三个维度解析。"),
        ("p5", "版本测评", "cp-bikeng", "散人玩家避坑指南五类版本", "分析快餐服、氪金服、合区服等常见陷阱。"),
        ("p6", "玩家交流", "jl-shaba-gongcheng", "沙巴克攻城战经典战役回顾", "重温那些年一起攻城的激情岁月。"),
    ]
    slides = []
    for i, (pcls, cat, slug, title, desc) in enumerate(focus_arts):
        active = " active" if i == 0 else ""
        slides.append(
            f'<div class="focus-slide{active}"><div class="ph {pcls}">{cat}</div>'
            f'<div class="cap"><b><a href="{slug}.html" style="color:#fff">{esc(title)}</a></b>'
            f'<span>{esc(desc)}</span></div></div>'
        )
    focus_slides = "\n".join(slides)

    kf_data = [
        ("10:00", "龙渊复古 1.80 经典重制", "复古", "fg-1-80-yuanban"),
        ("12:30", "战神合击 英雄觉醒版", "合击", "hj-heji-zuhe"),
        ("14:00", "一刀单职业 散人天堂", "单职业", "dz-weihe-huanying"),
        ("15:00", "热血微变 装备全靠打", "微变", "cp-wei-bian"),
        ("16:00", "沉默版本 经典重燃", "复古", "fg-jiuping"),
        ("18:00", "英雄连击 跨服争霸", "合击", "hj-lianji"),
        ("20:00", "迷失单职业 切割进化", "单职业", "dz-qidao"),
        ("22:00", "轻变三职业 散人起步", "轻变", "cp-quming"),
    ]
    kf_rows = ""
    for time, name, ctype, slug in kf_data:
        cat_key = "fugu" if "复古" in ctype else "xinkai"
        if ctype == "合击": cat_key = "heji"
        if ctype == "单职业": cat_key = "danzhiye"
        kf_rows += (
            f'<tr><td>{time}</td><td><a href="{slug}.html">{esc(name)}</a></td>'
            f'<td><a href="{cat_key}.html">{ctype}</a></td></tr>\n'
        )

    # 开服列表 - 纯文字无缩略图
    kaifu_data = [
        ("10:00", "龙渊复古 1.80 经典重制", "fg-1-80-yuanban", "复古"),
        ("12:30", "战神合击 英雄觉醒版", "hj-heji-zuhe", "合击"),
        ("14:00", "一刀单职业 散人天堂", "dz-weihe-huanying", "单职"),
        ("15:00", "热血微变 装备全靠打", "cp-wei-bian", "微变"),
        ("16:00", "沉默版本 经典重燃", "fg-jiuping", "复古"),
        ("18:00", "英雄连击 跨服争霸", "hj-lianji", "合击"),
        ("20:00", "迷失单职业 切割进化", "dz-qidao", "单职"),
        ("22:00", "轻变三职业 散人起步", "cp-quming", "轻变"),
    ]
    kaifu_list = ""
    for tm, name, slug, tag in kaifu_data:
        kaifu_list += (
            f'<li><span class="kf-time">{tm}</span>'
            f'<span class="kf-name"><a href="{slug}.html">{esc(name)}</a></span>'
            f'<span class="kf-tag">{tag}</span></li>\n'
        )

    all_arts = []
    for cat_key in CAT_INFO:
        all_arts.extend(articles_by_cat.get(cat_key, []))
    all_arts.sort(key=lambda a: a["date"], reverse=True)
    news_html = ""
    cat_badge = {
        "gonglue": "攻略", "xinkai": "开服", "ceping": "测评",
        "jiaoliu": "交流", "heji": "合击", "danzhiye": "单职", "fugu": "复古"
    }
    for a in all_arts[:12]:
        badge = cat_badge.get(a["cat"], a["cat_name"])
        news_html += (
            f'<li><i>{esc(badge)}</i><a href="{a["slug"]}.html">{esc(a["h1"])}</a>'
            f'<time>{a["date"]}</time></li>\n'
        )

    cat_blocks = ""
    for cat_key in ["xinkai", "fugu", "heji", "danzhiye", "gonglue", "ceping"]:
        info = CAT_INFO[cat_key]
        cat_arts = articles_by_cat.get(cat_key, [])[:6]
        items = ""
        for a in cat_arts:
            items += f'<li><a href="{a["slug"]}.html">{esc(a["h1"])}</a><time>{a["date"]}</time></li>\n'
        cat_blocks += (
            f'<div class="block"><div class="block-hd"><h2><a href="{info["url"]}">{info["name"]}</a></h2>'
            f'<a class="more" href="{info["url"]}">&raquo;</a></div>'
            f'<div class="block-bd"><ul class="list-news">{items}</ul></div></div>\n'
        )

    rank_data = [
        ("一刀单职业 散人天堂", "dz-weihe-huanying"),
        ("龙渊复古 1.80 经典重制", "fg-1-80-yuanban"),
        ("战神合击 英雄觉醒版", "hj-heji-zuhe"),
        ("热血微变 装备全靠打", "cp-wei-bian"),
        ("沉默版本 经典重燃", "fg-jiuping"),
        ("英雄连击 跨服争霸", "hj-lianji"),
        ("迷失单职业 切割进化", "dz-qidao"),
        ("轻变三职业 散人起步", "cp-quming"),
    ]
    rank_cls_list = [" top", " top2", " top3"]
    rank_right = ""
    for i, (name, slug) in enumerate(rank_data):
        cls = rank_cls_list[i] if i < 3 else ""
        rank_right += (
            f'<li class="{cls.strip()}"><span class="rank-num">{i+1}</span>'
            f'<span class="rt"><a href="{slug}.html">{esc(name)}</a></span></li>\n'
        )

    content = INDEX_BODY
    content = content.replace("__FOCUS_SLIDES__", focus_slides)
    content = content.replace("__KF_ROWS__", kf_rows)
    content = content.replace("__KAIFU_LIST__", kaifu_list)
    content = content.replace("__INDEX_NEWS__", news_html)
    content = content.replace("__INDEX_CAT_BLOCKS__", cat_blocks)
    content = content.replace("__RANK_ITEMS_RIGHT__", rank_right)

    ctx = {
        "__TITLE__": "新开传奇网站_今日新开传奇开服表_复古合击单职业传奇版本测评",
        "__KEYWORDS__": "新开传奇网站,今日新开传奇,传奇开服表,复古传奇,英雄合击,单职业传奇,传奇攻略,版本测评",
        "__DESCRIPTION__": "新开传奇网站每日更新最新传奇开服表，覆盖1.80复古、英雄合击、单职业、微变等版本，提供版本测评、新手攻略与玩家交流。",
        "__CANONICAL__": f"{SITE_URL}/",
        "__CSS__": "base.css",
        "__JS__": "base.js",
        "__NAV__": nav_html("home"),
        "__KEY__": "home",
        "__CONTENT__": content,
    }

    return render_template(TEMPLATE, ctx)

# ============ 文章页生成 ============

def build_article(a, articles_by_cat):
    sections_html = ""
    for h2, body in a["sections"]:
        sections_html += f"<h2>{esc(h2)}</h2>\n{body}\n"

    slug_map = {}
    for cat_arts in articles_by_cat.values():
        for ca in cat_arts:
            slug_map[ca["slug"]] = ca

    rel_links = []
    for slug in a["related"]:
        if slug in slug_map:
            rel_links.append(f'<a href="{slug}.html">{esc(slug_map[slug]["h1"])}</a>')
    related_links = "&nbsp;&nbsp;".join(rel_links) if rel_links else ""

    related_items = ""
    for slug in a["related"]:
        if slug in slug_map:
            related_items += f'<li><a href="{slug}.html">{esc(slug_map[slug]["h1"])}</a></li>\n'

    all_arts = []
    for cat_arts in articles_by_cat.values():
        all_arts.extend(cat_arts)
    all_arts.sort(key=lambda x: int(x["read"].replace(",", "")), reverse=True)
    hot_items = ""
    for ha in all_arts[:6]:
        hot_items += f'<li><a href="{ha["slug"]}.html">{esc(ha["h1"])}</a></li>\n'

    xk_arts = articles_by_cat.get("xinkai", [])[:6]
    latest_items = ""
    for la in xk_arts:
        latest_items += f'<li><a href="{la["slug"]}.html">{esc(la["h1"])}</a></li>\n'

    view_rank = ""
    rank_cls2 = [" top", " top2", " top3"]
    for i, va in enumerate(all_arts[:8]):
        cls = rank_cls2[i] if i < 3 else ""
        view_rank += (
            f'<li class="{cls.strip()}"><span class="rank-num">{i+1}</span>'
            f'<span class="rt"><a href="{va["slug"]}.html">{esc(va["h1"][:20])}</a></span></li>\n'
        )

    tags_html = ""
    for t in a["tags"]:
        tags_html += f'<a href="{a["cat_url"]}">{esc(t)}</a>'

    cat_arts = articles_by_cat.get(a["cat"], [])
    idx = next((i for i, x in enumerate(cat_arts) if x["slug"] == a["slug"]), -1)
    next_link = ""
    if idx < len(cat_arts) - 1:
        na = cat_arts[idx + 1]
        next_link = f'<a href="{na["slug"]}.html">下一篇：{esc(na["h1"])} &raquo;</a>'
    elif len(cat_arts) > 1:
        na = cat_arts[0]
        next_link = f'<a href="{na["slug"]}.html">下一篇：{esc(na["h1"])} &raquo;</a>'

    content = ARTICLE_BODY
    content = content.replace("__H1__", esc(a["h1"]))
    content = content.replace("__DATE__", a["date"])
    content = content.replace("__READ__", a["read"])
    content = content.replace("__CAT_NAME__", a["cat_name"])
    content = content.replace("__CAT_URL__", a["cat_url"])
    content = content.replace("__CONTENT__", sections_html)
    content = content.replace("__RELATED_LINKS__", related_links)
    content = content.replace("__TAGS__", tags_html)
    content = content.replace("__NEXT_LINK__", next_link)
    content = content.replace("__RELATED_ITEMS__", related_items)
    content = content.replace("__HOT_ITEMS__", hot_items)
    content = content.replace("__LATEST_ITEMS__", latest_items)
    content = content.replace("__VIEW_RANK__", view_rank)

    title = f'{esc(a["h1"])} - 新开传奇网站'
    if len(title) > 70:
        title = title[:70] + "..."

    ctx = {
        "__TITLE__": title,
        "__KEYWORDS__": a["kw"],
        "__DESCRIPTION__": a["desc"],
        "__CANONICAL__": f"{SITE_URL}/{a['slug']}.html",
        "__CSS__": "base.css",
        "__JS__": "base.js",
        "__NAV__": nav_html(a["cat"]),
        "__KEY__": a["cat"],
        "__CONTENT__": content,
    }

    return render_template(TEMPLATE, ctx)

# ============ 栏目页生成 ============

def build_category(cat_key, articles_by_cat):
    info = CAT_INFO[cat_key]
    arts = articles_by_cat.get(cat_key, [])

    cat_items = ""
    for a in arts:
        cat_items += (
            f'<li><a href="{a["slug"]}.html">{esc(a["h1"])}</a>'
            f'<time>{a["date"]}</time></li>\n'
        )

    cat_nav = ""
    for k, name in NAV_ITEMS:
        cat_nav += f'<li><a href="{CAT_INFO[k]["url"]}">{name}</a></li>\n'

    all_arts = []
    for cat_arts in articles_by_cat.values():
        all_arts.extend(cat_arts)
    all_arts.sort(key=lambda x: int(x["read"].replace(",", "")), reverse=True)
    hot_items = ""
    for ha in all_arts[:6]:
        hot_items += f'<li><a href="{ha["slug"]}.html">{esc(ha["h1"])}</a></li>\n'

    content = CATEGORY_BODY
    content = content.replace("__CAT_NAME__", info["name"])
    content = content.replace("__COUNT__", str(len(arts)))
    content = content.replace("__CAT_DESC__", info["desc"])
    content = content.replace("__CAT_ITEMS__", cat_items)
    content = content.replace("__CAT_NAV__", cat_nav)
    content = content.replace("__HOT_ITEMS__", hot_items)

    ctx = {
        "__TITLE__": f'{info["name"]}_最新开服信息_新开传奇网站',
        "__KEYWORDS__": f'{info["name"]},传奇开服,{info["name"]}版本,新开传奇网站',
        "__DESCRIPTION__": info["desc"][:160] if len(info["desc"]) > 160 else info["desc"],
        "__CANONICAL__": f"{SITE_URL}/{info['url']}",
        "__CSS__": "base.css",
        "__JS__": "base.js",
        "__NAV__": nav_html(cat_key),
        "__KEY__": cat_key,
        "__CONTENT__": content,
    }

    return render_template(TEMPLATE, ctx)

# ============ 404页 ============

def build_404():
    content = """
<div class="wrap" style="text-align:center;padding:80px 0">
  <h1 style="font-size:72px;color:#c8161d;margin-bottom:20px">404</h1>
  <p style="font-size:18px;color:#666;margin-bottom:30px">抱歉，您访问的页面不存在或已被删除</p>
  <div style="display:flex;gap:16px;justify-content:center">
    <a href="index.html" style="background:#c8161d;color:#fff;padding:10px 30px;border-radius:4px">返回首页</a>
    <a href="xinkai.html" style="background:#f5f6f8;color:#333;padding:10px 30px;border-radius:4px">浏览开服表</a>
  </div>
</div>
"""
    ctx = {
        "__TITLE__": "页面未找到 - 新开传奇网站",
        "__KEYWORDS__": "404,页面未找到,新开传奇网站",
        "__DESCRIPTION__": "您访问的页面不存在或已被删除，请返回新开传奇网站首页继续浏览。",
        "__CANONICAL__": f"{SITE_URL}/404.html",
        "__CSS__": "base.css",
        "__JS__": "base.js",
        "__NAV__": nav_html(""),
        "__KEY__": "",
        "__CONTENT__": content,
    }
    return render_template(TEMPLATE, ctx)

# ============ sitemap.xml ============

def build_sitemap(articles_by_cat):
    urls = [f"{SITE_URL}/index.html"]
    for k in CAT_INFO:
        urls.append(f"{SITE_URL}/{CAT_INFO[k]['url']}")
    for cat_arts in articles_by_cat.values():
        for a in cat_arts:
            urls.append(f"{SITE_URL}/{a['slug']}.html")

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        xml += f'  <url><loc>{u}</loc><changefreq>daily</changefreq><priority>0.8</priority></url>\n'
    xml += '</urlset>'
    return xml

# ============ robots.txt ============

def build_robots():
    return f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""

# ============ 主流程 ============

def main():
    articles_by_cat = defaultdict(list)
    for a in ARTICLES:
        articles_by_cat[a["cat"]].append(a)
    for k in articles_by_cat:
        articles_by_cat[k].sort(key=lambda x: x["date"], reverse=True)

    # 生成首页
    with open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_index(articles_by_cat))
    print("  [OK] index.html")

    # 生成文章页
    ok = 0
    for a in ARTICLES:
        path = os.path.join(OUT_DIR, f"{a['slug']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(build_article(a, articles_by_cat))
        ok += 1
    print(f"  [OK] {ok} article pages")

    # 生成栏目页
    for k in CAT_INFO:
        path = os.path.join(OUT_DIR, CAT_INFO[k]["url"])
        with open(path, "w", encoding="utf-8") as f:
            f.write(build_category(k, articles_by_cat))
    print(f"  [OK] {len(CAT_INFO)} category pages")

    # 生成404
    with open(os.path.join(OUT_DIR, "404.html"), "w", encoding="utf-8") as f:
        f.write(build_404())
    print("  [OK] 404.html")

    # 生成sitemap
    with open(os.path.join(OUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(build_sitemap(articles_by_cat))
    print("  [OK] sitemap.xml")

    # 生成robots
    with open(os.path.join(OUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(build_robots())
    print("  [OK] robots.txt")

    total = 1 + len(ARTICLES) + len(CAT_INFO) + 1 + 1 + 1
    print(f"\n✅ 生成完成，共 {total} 个文件（全部平铺在根目录）")
    for k, v in articles_by_cat.items():
        print(f"  - {CAT_INFO[k]['name']}: {len(v)} 篇")

if __name__ == "__main__":
    main()
