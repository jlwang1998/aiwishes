from settings import DeepSeek_API_KEY
from langchain_deepseek import ChatDeepSeek
from pydantic import SecretStr
from langchain.agents import create_agent
from schemas.agent_schemas import NameSchema, NameResultSchema,WishSchema, WishResultSchema
from schemas.name_schemas import NameIn
from schemas.wish_schemas import WishIn
import asyncio

llm = ChatDeepSeek(
    model="deepseek-chat", 
    api_key=DeepSeek_API_KEY,
    temperature=0.9
    )

name_prompt = """
你是一位精通汉语言文学、音韵学与传统文化的命名专家，擅长为人物创作兼具音律美感、深刻寓意与文化内涵的姓名。请严格遵循以下原则进行命名：

发音优先：名字需平仄协调、声调起伏自然，避免拗口、谐音歧义（如不雅谐音、负面联想），朗朗上口，富有韵律感；
寓意深远：结合用户提供的背景（如姓氏、性别、字数和其他要求等），选取具有积极象征意义的意象（如自然元素、美德品质、经典典故），做到“名以载道”；
内涵厚重：优先从《诗经》《楚辞》《论语》等经典文献，或唐诗宋词、成语典故中汲取灵感，确保名字有出处、有底蕴，避免空洞堆砌；
现代适配：在尊重传统的基础上，兼顾当代语境与审美，避免过度古奥或生僻字（生僻字需附注音与释义），确保实用性与传播性；
个性化定制：根据用户具体需求（如性别倾向、字数限制、风格偏好——儒雅/清丽/大气/灵动等），提供5个候选方案，并按照以下格式输出：
【姓名】姓名
【出处】典籍来源或文化意象
【寓意】字义拆解与整体象征
"""

wish_prompt = """
你是一位祝福语生成大师，精通汉语言文学、音韵学与传统文化，擅长为特定人物与场景创作兼具音律美感、深刻寓意与文化内涵的祝语。你的核心使命是根据用户提供的具体信息，生成高度定制化、雅俗共赏的祝福语。
生成核心原则：
音韵为先：确保祝语平仄协调、声调起伏自然，朗朗上口，富有节奏与韵律感。严格避开口语中的拗口组合、不雅谐音或可能引发负面联想的读音。
寓意载道：深度结合用户提供的背景（如姓氏、性别、关系、祝语类型、祝语风格、字数等），精心选取具有积极、美好象征意义的自然意象、美德词汇或人文典故，使祝福言之有物，寓意深远。
文脉深厚：创作灵感应优先源自《诗经》、《楚辞》、《论语》、唐诗宋词及经典成语典故，确保祝语有文化根基与出处，避免辞藻的虚空堆砌。
古今融通：在恪守传统文韵的同时，兼顾现代汉语的通用性与当代审美。除非必要且能增强意境，否则慎用生僻字词；若使用，必须随文附上拼音与简要释义，以确保其传播性与实用性。
输出格式要求：
针对每次请求，你必须生成 5个​ 候选祝语方案。
每个方案严格遵循以下格式输出：
【祝语】（此处为祝福语全文，通常为2字、4字或对仗短句）
【寓意】（此处分两部分：
字义拆解：逐字或逐词解释其本义与在祝语中的引申义。
整体象征：阐述该祝语所融合的意象、典故及整体表达的祝福内涵。）
"""


name_agent = create_agent(
    model=llm,
    tools=[],
    system_prompt=name_prompt,
    response_format=NameResultSchema # 指定返回结果格式
)

with_agent = create_agent(
    model=llm,
    tools=[],
    system_prompt=wish_prompt,
    response_format=WishResultSchema # 输出结果格式
)

async def generate_names(name_info: NameIn) -> NameResultSchema:
    """生成姓名

    Args:
        name_info (NameIn): 姓名信息

    Returns:
        NameResultSchema: 姓名结果
    """
    prompt = f"用户姓氏是：{name_info.surname}，性别是：{name_info.gender}，名字字数要求是：{name_info.length}，其他要求是：{name_info.other}，这些名字不要：{'、'.join(name_info.exclude)}"
    result = await name_agent.ainvoke({
        "messages": [{'role': "user", "content": prompt}]
    })
    return result['structured_response']

async def generate_wishes(wish_info: WishIn) -> WishResultSchema:
    """生成祝福语

    Args:
        wish_info (WishIn): 祝福语信息

    Returns:
        WishResultSchema: 祝福语结果
    """
    prompt = f"用户姓名是：{wish_info.name}，性别是：{wish_info.gender}，关系是：{wish_info.relation}，祝语风格是：{wish_info.wish_style}，祝语类型是：{wish_info.wish_type,}，祝语字数不超过：{wish_info.wish_length}"
    result = await with_agent.ainvoke({
        "messages": [{'role': "user", "content": prompt}]
    })
    return result['structured_response']