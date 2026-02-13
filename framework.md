# Aegis Framework

## Vision
Aegis is an autonomous, self-evolving system designed to improve its own architecture, integrations, and performance. It leverages a modular "Lego" approach to development, where new capabilities are integrated as discrete components (Legos) and validated through an automated self-improvement cycle.

## Self-Improvement Cycle
1. **Reflect**: Analyze the current state of the project, including the `todo.md` and performance logs.
2. **Integrate**: Incorporate new components from `legos-dev/` into the core project.
3. **Test**: Run the project as a "serious user" to ensure tight integration and functional correctness.
4. **Evaluate**: Track performance metrics and log visual proof of improvement.
5. **Commit**: Use git to document the improvement and settle the latest changes.

## Core Setup
- **Terminal Access**: Integrated via `termpair`.
- **Authentication**: Managed through `authx`.
- **LLM Inference**: Powered by `llama.cpp`.
- **Workflow Automation**: Facilitated by `n8n-mcp`.
- **Security**: JWT Spring Security (JPA) for enterprise-grade protection.

## Development Principles
- **Holistic Testing**: Use integrations in extreme cases to ensure robustness.
- **Tight Integrations**: All parts must communicate seamlessly as stated in the documentation.
- **Visual Proof**: Every change must be backed by measurable performance or logging data.
