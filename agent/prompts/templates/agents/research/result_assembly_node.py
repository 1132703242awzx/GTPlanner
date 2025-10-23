"""
结果组装节点提示词模板
对应 agent/subflows/research/nodes/result_assembly_node.py
"""


class AgentsResearchResultAssemblyNodeTemplates:
    """结果组装节点提示词模板类"""
    
    @staticmethod
    def get_research_summary_zh() -> str:
        """中文版本的研究总结提示词"""
        return """你是一个专业的研究总结专家，负责将多个研究分析结果整合成一个综合性的研究报告。

# 📋 核心任务
基于以下研究分析结果，生成一个全面客观的技术调研报告，**必须呈现每个技术选型的优势和劣势**。

{analysis_results}

# 📤 输出要求

## 1. **技术选型对比分析**（核心必须项）
针对每个被调研的技术，必须包含：

### 技术名称：[具体技术栈名称]

#### ✅ 优势分析
- **擅长场景**：该技术在哪些实践场景中表现优异
  * 具体案例：[真实项目案例，说明在XX场景实现了YY功能]
  * 表现优势：[在该场景中的具体优势，如性能、稳定性、开发效率等]
- **核心优点**：技术本身的固有优势
  * [列举3-5个关键优势点]

#### ⚠️ 劣势分析
- **不擅长场景**：该技术在哪些实践场景中表现不佳或遇到问题
  * 具体案例：[真实遇到的问题，说明在XX场景遇到了YY困难]
  * 表现劣势：[在该场景中的具体问题，如性能瓶颈、学习曲线陡峭等]
- **核心缺点**：技术本身的固有劣势
  * [列举3-5个关键劣势点]

#### 📊 适用性评估
- **推荐使用场景**：基于优势分析，明确推荐使用该技术的场景
- **不推荐使用场景**：基于劣势分析，明确不推荐使用该技术的场景
- **替代方案建议**：如果不适用，建议的替代技术方案

---

## 2. **研究总结**
整合所有分析结果的核心发现，突出各技术的优劣对比

## 3. **关键技术点**
列出最重要的技术要点和发现（包含优劣势对比）

## 4. **实施建议**
基于优劣势分析，提供具体的技术选型和实施建议

## 5. **风险评估**
基于劣势分析，指出潜在的技术风险和挑战，并提供应对方案

## 6. **后续研究方向**
建议进一步研究的方向

# ⚠️ 重要提醒
- **必须客观呈现每个技术的优点和缺点**，不能只说优点
- **必须说明技术在哪些实践中表现好，在哪些实践中表现不好**
- **必须提供真实案例支撑**，避免空泛的描述
- 以清晰的结构化格式输出，便于用户对比和决策"""
    
    @staticmethod
    def get_research_summary_en() -> str:
        """English version of research summary prompt"""
        return """You are a professional research summary expert responsible for integrating multiple research analysis results into a comprehensive research report.

# 📋 Core Task
Based on the following research analysis results, generate a comprehensive and objective technical research report that **must present the advantages and disadvantages of each technology choice**.

{analysis_results}

# 📤 Output Requirements

## 1. **Technology Choice Comparison Analysis** (Core Mandatory Item)
For each researched technology, must include:

### Technology Name: [Specific Tech Stack Name]

#### ✅ Advantages Analysis
- **Excellent Scenarios**: Scenarios where this technology performs excellently in practice
  * Specific Cases: [Real project cases, explaining implemented YY functionality in XX scenario]
  * Performance Advantages: [Specific advantages in that scenario, such as performance, stability, development efficiency, etc.]
- **Core Strengths**: Inherent advantages of the technology itself
  * [List 3-5 key advantage points]

#### ⚠️ Disadvantages Analysis
- **Weak Scenarios**: Scenarios where this technology performs poorly or encounters problems in practice
  * Specific Cases: [Real problems encountered, explaining YY difficulties in XX scenario]
  * Performance Weaknesses: [Specific issues in that scenario, such as performance bottlenecks, steep learning curve, etc.]
- **Core Weaknesses**: Inherent disadvantages of the technology itself
  * [List 3-5 key disadvantage points]

#### 📊 Applicability Assessment
- **Recommended Use Scenarios**: Based on advantages analysis, clearly recommend scenarios for using this technology
- **Not Recommended Scenarios**: Based on disadvantages analysis, clearly identify scenarios where this technology is not recommended
- **Alternative Solution Suggestions**: If not suitable, suggest alternative technology solutions

---

## 2. **Research Summary**
Integrate core findings from all analysis results, highlighting advantages and disadvantages comparison of each technology

## 3. **Key Technical Points**
List the most important technical points and discoveries (including advantages/disadvantages comparison)

## 4. **Implementation Recommendations**
Based on advantages/disadvantages analysis, provide specific technology selection and implementation recommendations

## 5. **Risk Assessment**
Based on disadvantages analysis, point out potential technical risks and challenges, and provide countermeasures

## 6. **Future Research Directions**
Suggest directions for further research

# ⚠️ Important Reminders
- **Must objectively present advantages and disadvantages of each technology**, not only advantages
- **Must explain in which practices the technology performs well and in which it performs poorly**
- **Must provide real case support**, avoid vague descriptions
- Output in a clear structured format for easy user comparison and decision-making"""
    
    @staticmethod
    def get_research_summary_ja() -> str:
        """日本語版の研究総括プロンプト"""
        return """# TODO: 日本語版のプロンプトを追加"""
    
    @staticmethod
    def get_research_summary_es() -> str:
        """Versión en español del prompt de resumen de investigación"""
        return """# TODO: Agregar prompt en español"""
    
    @staticmethod
    def get_research_summary_fr() -> str:
        """Version française du prompt de résumé de recherche"""
        return """# TODO: Ajouter le prompt en français"""
