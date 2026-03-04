# Observability FAQ

## Q: What should we monitor in agentic systems?
A: Latency, token usage, tool failures, retrieval quality, guardrail blocks, and user satisfaction signals.

## Q: Why are traces important?
A: Traces connect planner decisions, tool calls, and outputs to debug failures quickly.

## Q: How do we evaluate answer quality?
A: Use groundedness checks, citation coverage, hallucination rate, and task success metrics.

## Q: What alerts are most useful?
A: Error spikes, timeout spikes, abnormal denial counts, and cost anomalies.

## Q: How often should evaluations run?
A: Run offline benchmark evaluations on every major change and periodic production sampling daily.
