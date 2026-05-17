"""
扫描项目目录中的所有PDF论文，提取文本内容，构建知识库。
排除个人文档（简历、CV）和项目报告。
"""
import os
import json
import fitz  # PyMuPDF

# 项目根目录
BASE_DIR = r'd:\success'
# 知识库输出目录
OUTPUT_DIR = r'd:\success\diffusion-exam-system'

# 排除的文件夹
EXCLUDE_DIRS = {'node_modules', '.git', 'sleep_monitoring', 'sleep_hand环', '各种项目', '实习', '创业想法', 'stylization', 'AI_comic', 'AIVtuber', 'uni', 'univer', 'normal', 'controllable video'}

# 排除的文件名关键词
EXCLUDE_KEYWORDS = {'resume', 'cv', '简历', '本科论文', '项目展示', 'final_report', 'convergence_plot', 'result_collage'}

def is_relevant_pdf(filepath, rel_path):
    """判断PDF是否与考试相关"""
    fname = os.path.basename(filepath).lower()
    
    # 排除个人文档
    for kw in EXCLUDE_KEYWORDS:
        if kw in fname:
            return False
    
    # 排除特定目录
    for excl in EXCLUDE_DIRS:
        if excl in rel_path.lower().replace('\\', '/'):
            return False
    
    return True

def extract_pdf_text(filepath, max_pages=15):
    """从PDF提取文本（限制页数避免过大）"""
    try:
        doc = fitz.open(filepath)
        total_pages = len(doc)
        pages_to_read = min(total_pages, max_pages)
        
        texts = []
        for i in range(pages_to_read):
            page = doc[i]
            text = page.get_text()
            if text.strip():
                texts.append(text)
        
        doc.close()
        
        full_text = '\n'.join(texts)
        
        return {
            'total_pages': total_pages,
            'pages_read': pages_to_read,
            'text_length': len(full_text),
            'text': full_text[:50000]  # 限制总长度
        }
    except Exception as e:
        return {'error': str(e), 'text': ''}

def categorize_paper(rel_path, filename):
    """根据路径分类论文"""
    path_lower = rel_path.lower().replace('\\', '/')
    fname_lower = filename.lower()
    
    categories = []
    
    if 'diffusion' in path_lower or '扩散' in path_lower or 'cold_diffusion' in path_lower:
        categories.append('diffusion_models')
    if '3d' in path_lower or 'nerf' in path_lower or 'gaussian' in path_lower or 'splatting' in path_lower:
        categories.append('3d_reconstruction')
    if 'video' in path_lower or 'cogvideo' in path_lower or 'animate' in path_lower:
        categories.append('video_generation')
    if 'time_series' in path_lower or 'timemixer' in path_lower or 'mamba' in path_lower:
        categories.append('time_series')
    if 'segdino' in path_lower or 'sam' in path_lower or 'segment' in path_lower or 'dino' in path_lower:
        categories.append('segmentation_representation')
    if 'multimodal' in path_lower or '多模态' in path_lower or 'blip' in path_lower or 'clip' in path_lower:
        categories.append('multimodal')
    if 'low_light' in path_lower or '低光' in path_lower or 'restoration' in path_lower:
        categories.append('image_restoration')
    if 'representation' in path_lower:
        categories.append('segmentation_representation')
    if 'meta' in path_lower and 'human' in path_lower:
        categories.append('digital_human')
    if 'guidance' in path_lower:
        categories.append('diffusion_models')
    if 'transporent' in path_lower or 'glass' in fname_lower:
        categories.append('image_restoration')
    if 'world_model' in path_lower:
        categories.append('world_model')
    if 'theory_diffusion' in path_lower or 'tri' in path_lower:
        categories.append('diffusion_models')
    if 'runmin' in path_lower or 'dong' in path_lower:
        categories.append('super_resolution')
    if 'taihanghu' in path_lower:
        categories.append('diffusion_models')
    if 'fastvideo' in path_lower:
        categories.append('video_generation')
    if 'icml' in path_lower:
        categories.append('diffusion_models')
    if '周弈帆' in path_lower or 'zhou' in path_lower:
        categories.append('diffusion_models')
    if '卢治合' in path_lower:
        categories.append('test_time_adaptation')
    if '本校老师' in path_lower or '陈仁章' in path_lower:
        categories.append('other_research')
    if '生成式' in path_lower:
        categories.append('diffusion_models')
    if 'autoregressive' in path_lower:
        categories.append('diffusion_models')
    if 'watermark' in path_lower or '数字水印' in path_lower:
        categories.append('other_research')
    if 'information_theory' in path_lower or 'selection_of_classifiers' in path_lower:
        categories.append('other_research')
    if 'agent' in path_lower:
        categories.append('other_research')
    
    if not categories:
        categories.append('uncategorized')
    
    return categories

def main():
    print("=" * 60)
    print("扫描PDF论文并提取内容...")
    print("=" * 60)
    
    pdf_files = []
    
    for root, dirs, files in os.walk(BASE_DIR):
        # 排除不需要的目录
        dirs[:] = [d for d in dirs if d.lower() not in EXCLUDE_DIRS and not d.startswith('.')]
        
        for f in files:
            if f.lower().endswith('.pdf'):
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, BASE_DIR)
                
                if is_relevant_pdf(full_path, rel_path):
                    pdf_files.append((full_path, rel_path, f))
    
    print(f"\n找到 {len(pdf_files)} 个相关PDF文件")
    
    knowledge_base = []
    errors = []
    
    for i, (full_path, rel_path, filename) in enumerate(pdf_files):
        print(f"\n[{i+1}/{len(pdf_files)}] 处理: {filename}")
        
        # 提取文本
        result = extract_pdf_text(full_path)
        
        if 'error' in result:
            print(f"  ❌ 错误: {result['error']}")
            errors.append((filename, result['error']))
            continue
        
        # 分类
        categories = categorize_paper(rel_path, filename)
        
        # 提取标题（从文件名）
        title = os.path.splitext(filename)[0]
        # 清理arXiv编号等
        if 'v1' in title or 'v2' in title or 'v3' in title:
            title = title.rsplit('v', 1)[0].rstrip('.')
        title = title.replace('_', ' ').strip()
        
        entry = {
            'filename': filename,
            'rel_path': rel_path,
            'title': title,
            'categories': categories,
            'total_pages': result['total_pages'],
            'text_length': result['text_length'],
            'text': result['text']
        }
        
        knowledge_base.append(entry)
        print(f"  ✓ 分类: {categories}, 页数: {result['total_pages']}, 文本长度: {result['text_length']}")
    
    # 保存知识库
    kb_path = os.path.join(OUTPUT_DIR, 'knowledge_base.json')
    with open(kb_path, 'w', encoding='utf-8') as f:
        json.dump(knowledge_base, f, ensure_ascii=False, indent=2)
    
    print(f"\n{'=' * 60}")
    print(f"知识库已保存: {kb_path}")
    print(f"成功提取: {len(knowledge_base)} 篇论文")
    print(f"失败: {len(errors)} 篇")
    
    # 统计分类
    cat_count = {}
    for entry in knowledge_base:
        for cat in entry['categories']:
            cat_count[cat] = cat_count.get(cat, 0) + 1
    
    print(f"\n分类统计:")
    for cat, count in sorted(cat_count.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count}篇")
    
    # 总文本量
    total_text = sum(e['text_length'] for e in knowledge_base)
    print(f"\n总文本量: {total_text:,} 字符 ({total_text/1024/1024:.1f} MB)")

if __name__ == '__main__':
    main()
