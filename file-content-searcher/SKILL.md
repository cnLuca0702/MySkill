---
name: file-content-searcher
description: 文件内容搜索工具。当用户提到搜索文件内容、查找包含关键词的文件、在文件夹中搜索特定文本时触发。支持递归搜索目录，找出包含指定内容的所有文件。
---

# 文件内容搜索工具

## 功能说明

帮助用户在目录中递归搜索文件内容，找出包含指定关键词的所有文件。

## 适用场景

- 从一批文件中找出包含特定项目名称的文件
- 文件名是数字或其他无意义字符，需要按内容筛选
- 批量搜索多个文件中的特定文本

## 使用方法

### 1. 检查工具是否安装

首先检查系统是否已安装 ripgrep：

```bash
which rg || echo "NOT_INSTALLED"
```

### 2. 如果未安装，指导用户安装

**Linux/Ubuntu:**
```bash
sudo apt install ripgrep
```

**macOS:**
```bash
brew install ripgrep
```

**Windows:**
```powershell
# 方法 1：winget
winget install BurntSushi.ripgrep

# 方法 2：chocolatey
choco install ripgrep

# 方法 3：scoop
scoop install ripgrep
```

### 3. 执行搜索

当用户要求搜索文件内容时，使用以下命令：

```bash
# 基础搜索：找出包含关键词的所有文件（只显示文件名）
rg -l "关键词" /path/to/search/

# 递归搜索当前目录
rg -l "关键词" .

# 显示匹配的内容（带行号）
rg "关键词" /path/to/search/

# 显示匹配的内容及上下文（前后各 3 行）
rg -C 3 "关键词" /path/to/search/

# 忽略大小写
rg -li "关键词" /path/to/search/

# 只搜索特定文件类型（如 .txt, .log）
rg -l "关键词" -t txt /path/to/search/
rg -l "关键词" --type log /path/to/search/

# 搜索多个关键词（任一匹配）
rg -l "关键词1|关键词2" /path/to/search/

# 搜索多个关键词（全部匹配）
rg -l "关键词1" /path/to/search/ | xargs rg -l "关键词2"
```

## 输出格式说明

### -l 参数输出（只显示文件名）
```
/path/to/file1.txt
/path/to/file2.log
/path/to/dir/file3.md
```

### 不带 -l 参数输出（显示匹配的行）
```
/path/to/file1.txt:1:这是包含关键词的第一行
/path/to/file1.txt:5:这是包含关键词的第二行
/path/to/file2.log:10:另一个匹配行
```

## 注意事项

1. **路径处理**：如果用户没有提供完整路径，询问用户要搜索的目录
2. **权限问题**：如果遇到权限错误，使用 sudo 或检查目录权限
3. **大目录**：对于非常大的目录，搜索可能需要一些时间
4. **二进制文件**：ripgrep 默认跳过二进制文件，如需搜索使用 `-a` 参数

## 常见问题

**Q: 为什么搜不到文件？**
A: 检查路径是否正确，关键词是否正确，可能需要使用 `-i` 忽略大小写

**Q: 搜索很慢怎么办？**
A: 可以先用 `-t` 参数限定文件类型，减少搜索范围

**Q: 可以搜索压缩文件吗？**
A: 可以使用 ugrep 工具（支持 zip, tar.gz 等），但需要单独安装

## 示例对话

**用户**: 帮我搜索文件夹 /tmp/test 下的文件，找出包含 "项目名称" 的文件

**Agent**: 
```bash
# 先检查工具
which rg

# 执行搜索
rg -l "项目名称" /tmp/test/
```

**输出**:
```
/tmp/test/12345.txt
/tmp/test/67890.log
/tmp/test/11111.md
```

---

## 技术背景

- **ripgrep (rg)**: Rust 编写的超快搜索工具，比 grep 快 10 倍以上
- **尊重 .gitignore**: 默认忽略 git 忽略的文件
- **跨平台**: Linux、macOS、Windows 都支持