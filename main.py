structure = {
    "01第一部分 基础": {
    "第2章 算法基础": [
        "2.1 插入排序",
        "2.2 分析算法",
        "2.3 设计算法",
        {
            "2.3.1 分治法": [],
            "2.3.2 分析分治算法": []
        },
    ],
    "第3章 函数的增长": [
        "3.1 渐近记号",
        "3.2 标准记号与常用函数",
    ],
    "第4章 分治策略": [
        "4.1 最大子数组问题",
        "4.2 矩阵乘法的Strassen算法",
        "4.3 用代入法求解递归式",
        "4.4 用递归树方法求解递归式",
        "4.5 用主方法求解递归式",
        {
            "4.6 证明主定理": [
                "4.6.1 对b的幂证明主定理",
                "4.6.2 向下取整和向上取整"
            ]
        },
    ],
    "第5章 概率分析和随机算法": [
        "5.1 雇用问题",
        "5.2 指示器随机变量",
        "5.3 随机算法",
        {
            "5.4 概率分析和指示器随机变量的进一步使用": [
                "5.4.1 生日悖论",
                "5.4.2 球与箱子",
                "5.4.3 特征序列",
                "5.4.4 在线雇用问题"
            ]
        },
    ],
    },
    "02第二部分 排序和顺序统计量": {
        "第6章 堆排序": [
            "6.1 堆",
            "6.2 维护堆的性质",
            "6.3 建堆",
            "6.4 堆排序算法",
            "6.5 优先队列",
        ],
        "第7章 快速排序": [
            "7.1 快速排序的描述",
            "7.2 快速排序的性能",
            "7.3 快速排序的随机化版本",
            {
                "7.4 快速排序分析": [
                    "7.4.1 最坏情况分析",
                    "7.4.2 期望运行时间"
                ]
            },
        ],
        "第8章 线性时间排序": [
            "8.1 排序算法的下界",
            "8.2 计数排序",
            "8.3 基数排序",
            "8.4 桶排序",
        ],
        "第9章 中位数和顺序统计量": [
            "9.1 最小值和最大值",
            "9.2 期望为线性时间的选择算法",
            "9.3 最坏情况为线性时间的选择算法",
        ]
    },
    "03第三部分 数据结构": {
        "第10章 基本数据结构": [
            "10.1 栈和队列",
            "10.2 链表",
            "10.3 指针和对象的实现",
            "10.4 有根树的表示",
        ],
        "第11章 散列表": [
            "11.1 直接寻址表",
            "11.2 散列表",
            {
                "11.3 散列函数": [
                    "11.3.1 除法散列法",
                    "11.3.2 乘法散列法",
                    "11.3.3 全域散列法"
                ]
            },
            "11.4 开放寻址法",
            "11.5 完全散列",
        ],
        "第12章 二叉搜索树": [
            "12.1 什么是二叉搜索树",
            "12.2 查询二叉搜索树",
            "12.3 插入和删除",
            "12.4 随机构建二叉搜索树",
        ],
        "第13章 红黑树": [
            "13.1 红黑树的性质",
            "13.2 旋转",
            "13.3 插入",
            "13.4 删除",
        ],
        "第14章 数据结构的扩张": [
            "14.1 动态顺序统计",
            "14.2 如何扩张数据结构",
            "14.3 区间树",
        ]
    },
    "04第四部分 高级设计和分析技术": {
        "第15章 动态规划": [
            "15.1 钢条切割",
            "15.2 矩阵链乘法",
            "15.3 动态规划原理",
            "15.4 最长公共子序列",
            "15.5 最优二叉搜索树",
        ],
        "第16章 贪心算法": [
            "16.1 活动选择问题",
            "16.2 贪心算法原理",
            "16.3 赫夫曼编码",
            {
                "16.4 拟阵和贪心算法": [
                    "16.5 用拟阵求解任务调度问题"
                ]
            },
        ],
        "第17章 摊还分析": [
            "17.1 聚合分析",
            "17.2 核算法",
            "17.3 势能法",
            {
                "17.4 动态表": [
                    "17.4.1 表扩张",
                    "17.4.2 表扩张和收缩"
                ]
            },
        ]
    },
    "05第五部分 高级数据结构": {
        "第18章 B树": [
            "18.1 B树的定义",
            "18.2 B树上的基本操作",
            "18.3 从B树中删除关键字",
        ],
        "第19章 斐波那契堆": [
            "19.1 斐波那契堆结构",
            "19.2 可合并堆操作",
            "19.3 关键字减值和删除一个结点",
            "19.4 最大度数的界",
        ],
        "第20章 van Emde Boas树": [
            "20.1 基本方法",
            "20.2 递归结构",
            {
                "20.2.1 原型van Emde Boas结构": [
                    "20.2.2 原型van Emde Boas结构上的操作"
                ]
            },
            {
                "20.3 van Emde Boas树及其操作": [
                    "20.3.1 van Emde Boas树",
                    "20.3.2 van Emde Boas树的操作"
                ]
            },
        ],
        "第21章 用于不相交集合的数据结构": [
            "21.1 不相交集合的操作",
            "21.2 不相交集合的链表表示",
            "21.3 不相交集合森林",
            "21.4 带路径压缩的按秩合并的分析",
        ]
    },
    "06第六部分 图算法": {
        "第22章 基本的图算法": [
            "22.1 图的表示",
            "22.2 广度优先搜索",
            "22.3 深度优先搜索",
            "22.4 拓扑排序",
            "22.5 强连通分量",
        ],
        "第23章 最小生成树": [
            "23.1 最小生成树的形成",
            "23.2 Kruskal算法和Prim算法",
        ],
        "第24章 单源最短路径": [
            "24.1 Bellman-Ford算法",
            "24.2 有向无环图中的单源最短路径问题",
            "24.3 Dijkstra算法",
            "24.4 差分约束和最短路径",
            "24.5 最短路径性质的证明",
        ],
        "第25章 所有结点对的最短路径问题": [
            "25.1 最短路径和矩阵乘法",
            "25.2 Floyd-Warshall算法",
            "25.3 用于稀疏图的Johnson算法",
        ],
        "第26章 最大流": [
            "26.1 流网络",
            "26.2 Ford-Fulkerson方法",
            "26.3 最大二分匹配",
            "26.4 推送重贴标签算法",
            "26.5 前置重贴标签算法",
        ]
    },
    "07第七部分 算法问题选编": {
        "第27章 多线程算法": [
            "27.1 动态多线程基础",
            "27.2 多线程矩阵乘法",
            "27.3 多线程归并排序",
        ],
        "第28章 矩阵运算": [
            "28.1 求解线性方程组",
            "28.2 矩阵求逆",
            "28.3 对称正定矩阵和最小二乘逼近",
        ],
        "第29章 线性规划": [
            "29.1 标准型和松弛型",
            "29.2 将问题表达为线性规划",
            "29.3 单纯形算法",
            "29.4 对偶性",
            "29.5 初始基本可行解",
        ],
        "第30章 多项式与快速傅里叶变换": [
            "30.1 多项式的表示",
            "30.2 DFT与FFT",
            "30.3 高效FFT实现",
        ],
        "第31章 数论算法": [
            "31.1 基础数论概念",
            "31.2 最大公约数",
            "31.3 模运算",
            "31.4 求解模线性方程",
            "31.5 中国余数定理",
            "31.6 元素的幂",
            "31.7 RSA公钥加密系统",
            "31.8 素数的测试",
            "31.9 整数的因子分解",
        ],
        "第32章 字符串匹配": [
            "32.1 朴素字符串匹配算法",
            "32.2 Rabin-Karp算法",
            "32.3 利用有限自动机进行字符串匹配",
            "32.4 Knuth-Morris-Pratt算法",
        ],
        "第33章 计算几何学": [
            "33.1 线段的性质",
            "33.2 确定任意一对线段是否相交",
            "33.3 寻找凸包",
            "33.4 寻找最近点对",
        ],
        "第34章 NP完全性": [
            "34.1 多项式时间",
            "34.2 多项式时间的验证",
            "34.3 NP完全性与可归约性",
            "34.4 NP完全性的证明",
            {
                "34.5 NP完全问题": [
                    "34.5.1 团问题",
                    "34.5.2 顶点覆盖问题",
                    "34.5.3 哈密顿回路问题",
                    "34.5.4 旅行商问题",
                    "34.5.5 子集和问题"
                ]
            },
        ],
        "第35章 近似算法": [
            "35.1 顶点覆盖问题",
            {
                "35.2 旅行商问题": [
                    "35.2.1 满足三角不等式的旅行商问题",
                    "35.2.2 一般旅行商问题"
                ]
            },
            "35.3 集合覆盖问题",
            "35.4 随机化和线性规划",
            "35.5 子集和问题",
        ]
    }
}

import os
import json
from typing import Union, Dict, List, Any

def create_directories_and_files(
    base_path: str, 
    structure: Dict[str, Any], 
    readme_file, 
    parent_path: str = "", 
    level: int = 1
):
    """
    根据给定的目录结构创建目录和文件，并生成 README.md 文件。

    Args:
        base_path (str): 根目录路径。
        structure (Dict[str, Any]): 目录结构的嵌套字典。
        readme_file (File): 用于写入README内容的文件对象。
        parent_path (str): 父目录路径。
        level (int): 目录的层级，用于确定 README 标题级别。

    Returns:
        None
    """
    heading = "#" * level

    for key, value in structure.items():
        current_path = os.path.join(base_path, key.replace(" ", "_").replace("-", "_"))

        # 创建目录
        os.makedirs(current_path, exist_ok=True)

        # 在README中添加章节标题
        if parent_path:
            readme_file.write(f"{heading} {parent_path}/{key}\n\n")
        else:
            readme_file.write(f"{heading} {key}\n\n")

        # 递归调用创建子目录和文件
        if isinstance(value, dict) and value:
            create_directories_and_files(
                current_path, 
                value, 
                readme_file, 
                parent_path + "/" + key if parent_path else key, 
                level + 1
            )
        elif isinstance(value, list):
            for idx, item in enumerate(value):
                if isinstance(item, dict) and item:
                    create_directories_and_files(
                        current_path, 
                        item, 
                        readme_file, 
                        parent_path + "/" + key if parent_path else key, 
                        level + 1
                    )
                else:
                    item = f"{idx:02d}_{item}"
                    file_name = item.replace(" ", "_").replace("-", "_") + ".py"
                    file_path = os.path.join(current_path, file_name)
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(f"# {item}\n\n")
                        file.write(f'"""\nLecture: {parent_path}/{key}\nContent: {item}\n"""\n\n')

                    # 在README中添加文件链接
                    item_clean = item.replace(" ", "_").replace("-", "_")
                    parent_clean = parent_path.replace(" ", "_").replace("-", "_")
                    key_clean = key.replace(" ", "_").replace("-", "_")
                    readme_file.write(f"- [{item}](./{parent_clean}/{key_clean}/{item_clean}.py)\n")
        else:
            # 创建文件并写入初始内容
            file_name = key.replace(" ", "_").replace("-", "_") + ".py"
            file_path = os.path.join(current_path, file_name)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"# {key}\n\n")
                file.write(f'"""\nLecture: {parent_path}/{key}\nContent: {key}\n"""\n\n')

            # 在README中添加文件链接
            parent_clean = parent_path.replace(" ", "_").replace("-", "_")
            key_clean = key.replace(" ", "_").replace("-", "_")
            readme_file.write(f"- [{key}](./{parent_clean}/{key_clean}/{file_name})\n")

        # 添加空行以分隔不同的章节
        readme_file.write("\n")

def main():
    root_dir = './'
    # 创建根目录
    os.makedirs(root_dir, exist_ok=True)

    # 创建 README.md 文件
    with open(os.path.join(root_dir, "README.md"), 'w', encoding='utf-8') as readme_file:
        readme_file.write("# 算法导论\n\n")
        readme_file.write("这是一个关于算法导论的目录结构。\n\n")
        create_directories_and_files(root_dir, structure, readme_file)

    print("目录和文件结构已生成，并创建 README.md 文件。")

if __name__ == "__main__":
    main()