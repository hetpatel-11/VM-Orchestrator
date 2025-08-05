# 🧠 VM-Orchestrator: Multi-VM Task Orchestration System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Orgo AI](https://img.shields.io/badge/Powered%20by-Orgo%20AI-purple.svg)](https://orgo.ai)

> 🚀 **AI-powered VM orchestration system for intelligent task delegation across multiple virtual machines - built in 4 hours for hackathon innovation.**

## 🌟 Overview

VM-Orchestrator is a proof-of-concept distributed computing system that demonstrates task delegation across multiple virtual machines with file-based data sharing. Built on the Orgo AI platform with Claude integration, it explores the potential of collaborative AI computing.

## 🔥 Key Features

### 🧠 **Shared Memory Concept**
- **Unified File Access**: All VMs read/write to the same structured file
- **Data Synchronization**: Sequential updates across all machines
- **Structured Sections**: Organized file layout for each VM's contributions
- **Efficient Access**: Direct file operations for data sharing

### 🔗 **VM Interconnection**
- **Data Pipeline**: VM1 → VM2 → VM3 with file handoffs
- **Sequential Workflow**: Each VM builds on previous VM's work
- **Status Announcements**: VMs report data sharing progress
- **Progress Monitoring**: Real-time status updates of workflow

### ⚡ **Task Delegation**
- **Single Prompt Input**: Enter any task, system splits it intelligently
- **AI-Powered Analysis**: Claude analyzes prompts for task distribution
- **Adaptive Workflows**: Handles research, business, or creative tasks
- **Output Generation**: Creates presentations, analyses, and reports

## 🏗️ Architecture

```
┌─────────────┐    ┌─────────────────┐    ┌─────────────┐
│   VM1       │    │  SHARED FILE    │    │    VM3      │
│  Research   │◄──►│   SYSTEM        │◄──►│Presentation │
│             │    │                 │    │             │
└─────────────┘    └─────────────────┘    └─────────────┘
                           ▲
                           │
                   ┌─────────────┐
                   │    VM2      │
                   │ Processing  │
                   │             │
                   └─────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Orgo AI API key
- Anthropic Claude API key

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/hetpatel-11/VM-Orchestrator.git
cd VM-Orchestrator
```

2. **Install dependencies**
```bash
pip install orgo anthropic python-dotenv
```

3. **Configure API keys**
Create a `.env` file:
```env
ORGO_API_KEY=your_orgo_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
```

4. **Update VM Project IDs**
Edit the orchestrator files with your Orgo project IDs:
```python
self.vm1 = Computer(project_id="your-vm1-id", api_key=self.api_key)
self.vm2 = Computer(project_id="your-vm2-id", api_key=self.api_key)
self.vm3 = Computer(project_id="your-vm3-id", api_key=self.api_key)
```

## 🎯 Usage

### 🧠 Shared Memory Orchestrator (Recommended)
```bash
python3 shared_memory_orchestrator.py
```
**Best for**: Demonstrating shared file concept

### 👁️ Visible Interconnected Orchestrator
```bash
python3 visible_interconnected_orchestrator.py
```
**Best for**: Clear visualization of VM interconnection

### 🔗 Interconnected VM Orchestrator
```bash
python3 interconnected_vm_orchestrator.py
```
**Best for**: Data pipeline demonstration

### ⚡ Ultra-Optimized Orchestrator
```bash
python3 ultra_optimized_orchestrator.py
```
**Best for**: Speed-focused execution

## 📊 Example Workflows

### Research Analysis Pipeline
```
Input: "Research renewable energy market trends"
├── VM1: Market research & data collection
├── VM2: Statistical analysis & trend visualization  
└── VM3: Executive presentation with insights
```

### Business Intelligence Workflow
```
Input: "Create a business plan for AI startup"
├── VM1: Market research & competitive analysis
├── VM2: Financial modeling & projections
└── VM3: Investor-ready business presentation
```

### Creative Content Development
```
Input: "Design a marketing campaign for electric vehicles"
├── VM1: Target audience research & trends
├── VM2: Campaign strategy & content framework
└── VM3: Creative materials & presentation deck
```

## 🎪 Demo Features

- **10-15 minute execution** with visible interconnection
- **Professional deliverables** (presentations, spreadsheets, reports)
- **Real-time monitoring** of VM collaboration
- **Progress announcements** of data sharing
- **Live status updates** showing workflow progress

## 🛠️ Technical Details

### Built With
- **Python 3.8+** - Core language
- **Orgo AI** - VM orchestration platform
- **Claude API** - Natural language processing
- **Threading** - Parallel execution management
- **File I/O** - Data sharing between VMs

### Key Components
- **Task Analysis Engine** - AI-powered prompt interpretation
- **File Management System** - Shared data coordination
- **Workflow Orchestrator** - VM execution management
- **Progress Monitor** - Live status tracking
- **Output Generator** - Professional deliverable creation

## 🏆 Hackathon Innovation

This project was developed in **4 hours** for distributed computing exploration, demonstrating:
- **Multi-VM orchestration** concepts
- **AI-powered task delegation** approaches
- **File-based data sharing** between VMs
- **Collaborative computing** workflows
- **Rapid prototyping** in distributed systems

## 📈 Performance

- **Execution Time**: 10-15 minutes for complete workflow
- **VM Efficiency**: Parallel and sequential execution
- **File Management**: Structured data sharing
- **Scalability**: Extensible to more VMs
- **Reliability**: Basic error handling

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Acknowledgments

- **Orgo AI** - For the VM orchestration platform
- **Anthropic** - For Claude AI integration
- **Hackathon Community** - For inspiration and innovation

## 📞 Contact

**Het Patel** - [@hetpatel-11](https://github.com/hetpatel-11)

Project Link: [https://github.com/hetpatel-11/VM-Orchestrator](https://github.com/hetpatel-11/VM-Orchestrator)

---

⭐ **Star this repo if you found it helpful!** ⭐ 
