"""
LLM分析节点提示词模板
对应 agent/subflows/research/nodes/llm_analysis_node.py
"""


class AgentsResearchLlmAnalysisNodeTemplates:
    """LLM分析节点提示词模板类"""
    
    @staticmethod
    def get_research_analysis_zh() -> str:
        """中文版本的研究分析提示词"""
        return """你是一个专业的内容分析专家，擅长从大量文本中提取关键信息和洞察。

# 🎯 你的任务
1. 分析给定的内容，重点关注与指定关键词相关的信息
2. **全面提取技术的优势和劣势**，必须客观呈现
3. **识别技术在不同实践场景中的表现**（擅长的场景 vs 不擅长的场景）
4. 提取核心要点和技术细节
5. 提供实用的建议和洞察
6. 严格按照指定的JSON格式输出结果

# 📥 分析内容

**关键词**: {keyword}

**分析要求**: {requirements}

**内容**:
{content}

# 📤 输出格式要求

必须严格按照以下JSON格式返回分析结果：

{{
    "summary": "核心内容总结（简要说明该技术的定位和主要用途）",
    "advantages": {{
        "strengths": ["优势1：具体说明", "优势2：具体说明", "优势3：具体说明"],
        "good_practices": [
            {{
                "scenario": "擅长场景描述（具体实践场景）",
                "reason": "为什么在这个场景表现好（具体原因和案例）"
            }}
        ]
    }},
    "disadvantages": {{
        "weaknesses": ["劣势1：具体说明", "劣势2：具体说明", "劣势3：具体说明"],
        "poor_practices": [
            {{
                "scenario": "不擅长场景描述（具体实践场景）",
                "reason": "为什么在这个场景表现不好（具体问题和案例）"
            }}
        ]
    }},
    "key_points": ["要点1", "要点2", "要点3"],
    "relevance": "与{keyword}的相关性说明",
    "recommendations": [
        {{
            "type": "推荐使用" 或 "谨慎使用" 或 "不推荐使用",
            "scenario": "具体场景",
            "reason": "推荐理由"
        }}
    ]
}}

# ⚠️ 重要提醒
- **必须客观分析优势和劣势**，不能只说优点
- **advantages.good_practices 至少提供 2-3 个擅长的实践场景**
- **disadvantages.poor_practices 至少提供 1-2 个不擅长的实践场景**
- 必须返回有效的JSON格式
- 内容要简洁明了，避免冗余信息
- 基于实际案例和数据，避免空泛描述"""
    
    @staticmethod
    def get_research_analysis_en() -> str:
        """English version of research analysis prompt"""
        return """You are a professional content analysis expert skilled at extracting key information and insights from large amounts of text.

# 🎯 Your Tasks
1. Analyze the given content, focusing on information related to the specified keyword
2. **Comprehensively extract technology advantages and disadvantages**, must be objective
3. **Identify technology performance in different practical scenarios** (excellent scenarios vs. weak scenarios)
4. Extract core points and technical details
5. Provide practical suggestions and insights
6. Strictly output results in the specified JSON format

# 📥 Analysis Content

**Keyword**: {keyword}

**Analysis Requirements**: {requirements}

**Content**:
{content}

# 📤 Output Format Requirements

Must strictly return analysis results in the following JSON format:

{{
    "summary": "Core content summary (briefly explain the technology positioning and main use)",
    "advantages": {{
        "strengths": ["Advantage 1: specific explanation", "Advantage 2: specific explanation", "Advantage 3: specific explanation"],
        "good_practices": [
            {{
                "scenario": "Excellent scenario description (specific practical scenario)",
                "reason": "Why it performs well in this scenario (specific reasons and cases)"
            }}
        ]
    }},
    "disadvantages": {{
        "weaknesses": ["Weakness 1: specific explanation", "Weakness 2: specific explanation", "Weakness 3: specific explanation"],
        "poor_practices": [
            {{
                "scenario": "Weak scenario description (specific practical scenario)",
                "reason": "Why it performs poorly in this scenario (specific problems and cases)"
            }}
        ]
    }},
    "key_points": ["Point 1", "Point 2", "Point 3"],
    "relevance": "Relevance explanation with {keyword}",
    "recommendations": [
        {{
            "type": "Recommended" or "Use with Caution" or "Not Recommended",
            "scenario": "Specific scenario",
            "reason": "Recommendation reason"
        }}
    ]
}}

# ⚠️ Important Reminders
- **Must objectively analyze advantages and disadvantages**, not only advantages
- **advantages.good_practices must provide at least 2-3 excellent practical scenarios**
- **disadvantages.poor_practices must provide at least 1-2 weak practical scenarios**
- Must return valid JSON format
- Content should be concise and clear, avoiding redundant information
- Based on actual cases and data, avoid vague descriptions"""
    
    @staticmethod
    def get_research_analysis_ja() -> str:
        """日本語版の研究分析プロンプト"""
        return """# TODO: 日本語版のプロンプトを追加"""
    
    @staticmethod
    def get_research_analysis_es() -> str:
        """Versión en español del prompt de análisis de investigación"""
        return """# TODO: Agregar prompt en español"""
    
    @staticmethod
    def get_research_analysis_fr() -> str:
        """Version française du prompt d'analyse de recherche"""
        return """# TODO: Ajouter le prompt en français"""
