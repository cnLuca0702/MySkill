# 搜索引擎完整列表及使用方法

## 国内搜索引擎（8个）

### 1. 百度
**URL**: `https://www.baidu.com/s?wd={keyword}`
**用途**: 基础信息搜索、政府信息查询
**高级操作符**: 支持 site: filetype: "" - OR
**时间过滤器**: 不支持

**搜索示例**:
- 基础搜索: `银川金凤区`
- 站内搜索: `site:gov.cn 银川金凤区`
- 文件搜索: `银川金凤区 filetype:pdf`

### 2. 必应中国
**URL**: `https://cn.bing.com/search?q={keyword}&ensearch=0`
**用途**: 国内资讯搜索
**高级操作符**: 支持 site: filetype:
**时间过滤器**: 不支持

**搜索示例**:
- 资讯搜索: `银川经济发展`
- 官方信息: `site:yjinfeng.gov.cn 规划`

### 3. 必应国际
**URL**: `https://cn.bing.com/search?q={keyword}&ensearch=1`
**用途**: 国际资讯搜索
**高级操作符**: 支持 site: filetype:
**时间过滤器**: 不支持

**搜索示例**:
- 国际视角: `银川 国际投资`

### 4. 360
**URL**: `https://www.so.com/s?q={keyword}`
**用途**: 补充搜索
**高级操作符**: 支持 site:
**时间过滤器**: 不支持

**搜索示例**:
- 综合搜索: `银川 产业布局`

### 5. 搜狗
**URL**: `https://sogou.com/web?query={keyword}`
**用途**: 综合搜索
**高级操作符**: 支持 site:
**时间过滤器**: 不支持

**搜索示例**:
- 综合搜索: `银川 城市规划`

### 6. 微信
**URL**: `https://wx.sogou.com/weixin?type=2&query={keyword}`
**用途**: 微信公众号文章搜索
**高级操作符**: 不支持
**时间过滤器**: 不支持

**搜索示例**:
- 公众号: `银川统计`

### 7. 今日头条
**URL**: `https://so.toutiao.com/search?keyword={keyword}`
**用途**: 新闻资讯搜索
**高级操作符**: 不支持
**时间过滤器**: 不支持

**搜索示例**:
- 新闻: `银川 经济`

### 8. 集思录
**URL**: `https://www.jisilu.cn/explore/?keyword={keyword}`
**用途**: 金融投资搜索
**高级操作符**: 不支持
**时间过滤器**: 不支持

**搜索示例**:
- 金融: `银川 银行`

---

## 国际搜索引擎（9个）

### 1. Google
**URL**: `https://www.google.com/search?q={keyword}`
**用途**: 国际信息搜索、学术研究
**高级操作符**: 完整支持 site: filetype: "" - OR () ..
**时间过滤器**: 完整支持 tbs=qdr:{h|d|w|m|y}

**搜索示例**:
- 基础搜索: `银川 urban planning`
- 站内搜索: `site:gov.cn 中国 urban planning`
- 文件搜索: `urban planning filetype:pdf`
- 精确匹配: `"urban development"`
- 排除: `urban -realestate`
- 时间搜索: `urban news tbs=qdr:w`

### 2. Google HK
**URL**: `https://www.google.com.hk/search?q={keyword}`
**用途**: 香港视角搜索
**高级操作符**: 完整支持
**时间过滤器**: 完整支持

**搜索示例**:
- 香港视角: `银川 投资 香港`

### 3. DuckDuckGo
**URL**: `https://duckduckgo.com/html/?q={keyword}`
**用途**: 隐私搜索
**高级操作符**: 基础支持 - ""
**时间过滤器**: 不支持
**Bangs 快捷方式**: 支持 !g !gh !so !w 等

**搜索示例**:
- 隐私搜索: `银川 urban`
- Bangs: `!gh urban-analysis`

**Bangs 列表**:
| Bang | 目标 |
|------|------|
| `!g` | Google |
| `!gh` | GitHub |
| `!so` | Stack Overflow |
| `!w` | Wikipedia |
| `!yt` | YouTube |
| `!b` | Bing |
| `!a` | Amazon |
| `!y` | Yahoo |

### 4. Yahoo
**URL**: `https://search.yahoo.com/search?p={keyword}`
**用途**: 老牌搜索、雅虎资讯
**高级操作符**: 基础支持
**时间过滤器**: 不支持

**搜索示例**:
- 资讯: `Yinchuan urban`

### 5. Startpage
**URL**: `https://www.startpage.com/sp/search?query={keyword}`
**用途**: Google结果 + 隐私
**高级操作符**: 不直接支持
**时间过滤器**: 不支持

**搜索示例**:
- 隐私: `urban planning`

### 6. Brave
**URL**: `https://search.brave.com/search?q={keyword}`
**用途**: 独立索引搜索
**高级操作符**: 基础支持
**时间过滤器**: 不支持

**搜索示例**:
- 独立索引: `urban`

### 7. Ecosia
**URL**: `https://www.ecosia.org/search?q={keyword}`
**用途**: 环保搜索
**高级操作符**: 基础支持
**时间过滤器**: 不支持

**搜索示例**:
- 环保: `green city`

### 8. Qwant
**URL**: `https://www.qwant.com/?q={keyword}`
**用途**: GDPR合规、欧盟搜索
**高级操作符**: 基础支持
**时间过滤器**: 不支持

**搜索示例**:
- 欧盟视角: `Yinchuan Europe`

### 9. WolframAlpha
**URL**: `https://www.wolframalpha.com/input?i={keyword}`
**用途**: 知识计算、数学运算、数据查询
**高级操作符**: 不支持
**时间过滤器**: 不支持

**搜索示例**:
- 数学计算: `integrate x^2 dx`
- 货币转换: `100 USD to CNY`
- 股票查询: `AAPL stock`
- 天气查询: `weather in Beijing`
- 人口查询: `population of China`
- GDP查询: `GDP of China`

---

## 高级搜索技巧

### 站内搜索
```
site:gov.cn 银川金凤区 统计公报
site:yjinfeng.gov.cn 经济发展
site:tjj.yinchuan.gov.cn 人口
```

### 文件类型搜索
```
银川金凤区 filetype:pdf
银川金凤区 filetype:doc
银川金凤区 filetype:xlsx
```

### 精确匹配
```
"十四五"规划
"黄河流域生态保护"
```

### 排除关键词
```
银川 -房地产开发
银川 -旅游业
```

### 或运算
```
GDP OR 地区生产总值
城市规划 OR 城市规划
```

### 组合搜索
```
(site:gov.cn OR site:edu.cn) 银川 filetype:pdf
```

---

## Google 时间过滤器完整列表

| 参数 | 描述 | 时间范围 |
|------|------|---------|
| `tbs=qdr:h` | 过去1小时 | 最近1小时 |
| `tbs=qdr:d` | 过去24小时 | 最近1天 |
| `tbs=qdr:w` | 过去1周 | 最近7天 |
| `tbs=qdr:m` | 过去1月 | 最近30天 |
| `tbs=qdr:y` | 过去1年 | 最近365天 |

**自定义日期范围**:
```
tbs=cdr:1,cd_min:1/1/2024,cd_max:12/31/2024
```
2024年全年

---

## DuckDuckGo Bangs 完整列表

### 搜索引擎
| Bang | 目标 |
|------|------|
| `!g` | Google |
| `!b` | Bing |
| `!a` | Amazon |
| `!ddg` | DuckDuckGo |

### 编程开发
| Bang | 目标 |
|------|------|
| `!gh` | GitHub |
| `!so` | Stack Overflow |
| `!mdn` | MDN Web Docs |
| `!docs` | DevDocs |
| `!pypi` | PyPI |
| `!npm` | npmjs.com |
| `!docker` | Docker Hub |

### 知识百科
| Bang | 目标 |
|------|------|
| `!w` | Wikipedia |
| `!wen` | Wikipedia英文 |
| `!wt` | Wiktionary |
| `!imdb` | IMDb |

### 购物价格
| Bang | 目标 |
|------|------|
| `!a` | Amazon |
| `!e` | eBay |
| `!ali` | AliExpress |

---

## 搜索策略建议

### 数据收集策略
1. **多引擎验证**：同一关键词至少使用2-3个搜索引擎验证
2. **时间梯度**：先搜最新数据，再搜历史数据对比
3. **源优先级**：政府官网 > 权威媒体 > 统计平台 > 商业平台

### 搜索词优化
1. **使用官方名称**：如"银川市金凤区人民政府"而非"金凤区政府"
2. **包含年份**：如"2024年"、"2025年计划"
3. **使用 filetype**：优先搜索 PDF 文件，通常是官方报告
4. **组合关键词**：城市+关键词+年份+文件类型

### 避免搜索陷阱
1. **避免过窄关键词**：如"金凤区GDP2024年"可能无结果，应搜索"金凤区 GDP 2024"
2. **避免过宽关键词**：如"银川"结果太多，应加限定词
3. **避免非官方表述**：如用官方名称替代俗称
4. **避免拼音缩写**：使用全称避免歧义

---

## 常见问题

### Q1: 如何找到最新的统计公报？
**A**: 
1. 使用 `{城市名称} 统计公报 2024 filetype:pdf` 在 Google 或 百度搜索
2. 访问城市统计局官网的"统计公报"栏目
3. 查找自治区统计局网站的相关链接

### Q2: 如何搜索政府官方网站？
**A**:
1. 使用 `site:{城市官网域名} 关键词` 进行站内搜索
2. 常见域名格式：
   - `{城市拼音}.gov.cn` (如 ycjinfeng.gov.cn)
   - `{城市拼音}.yinchuan.gov.cn`
   - `{城市拼音}.nx.gov.cn` (宁夏)

### Q3: 如何搜索历史数据对比？
**A**:
1. 使用 `{城市名称} 统计公报 filetype:pdf` 搜索多个年份
2. 使用 `{城市名称} 历年数据 filetype:pdf` 搜索
3. 访问专业统计平台（如聚汇数据、红黑人口库）

### Q4: 如何搜索特定文件类型？
**A**:
1. Google/百度: `{关键词} filetype:{后缀}`
   - `filetype:pdf` (PDF文档)
   - `filetype:doc` (Word文档)
   - `filetype:xlsx` (Excel表格)
   - `filetype:ppt` (PowerPoint)
2. 搜索技巧：结合年份和机构名称

### Q5: 如何搜索多语言资源？
**A**:
1. 使用 Google HK 获取香港视角
2. 使用 WolframAlpha 进行数据计算和转换
3. 使用 DuckDuckGo 的隐私搜索功能
4. 使用特定国家的搜索引擎（如日本的 Yahoo!Japan）

---

## 搜索引擎性能对比

| 特性 | 百度 | Google | DuckDuckGo | WolframAlpha |
|------|------|--------|------------|---------------|
| 中文支持 | 优秀 | 良好 | 一般 | 良好 |
| 政府信息 | 优秀 | 良好 | 一般 | 一般 |
| 国际信息 | 一般 | 优秀 | 优秀 | 优秀 |
| 隐私保护 | 一般 | 差 | 优秀 | 优秀 |
| 高级操作 | 基础 | 完整 | 基础 | 无 |
| 时间过滤 | 无 | 完整 | 无 | 无 |
| 知识计算 | 无 | 无 | 无 | 完整 |
| Bangs | 无 | 无 | 支持 | 无 |

---

*更新时间：2026-03-20*
*版本：1.0*
