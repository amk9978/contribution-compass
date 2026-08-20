# AI Infrastructure — 2026-08-20

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [\[Ray Data\] Categorizer throws internal errors during doctest](https://github.com/ray-project/ray/issues/50285)

- Project: `ray-project/ray`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: good first issue; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [\[Data\] write_lance is incompatible with PyLance 6.x due to removed storage_options_provider argument](https://github.com/ray-project/ray/issues/65129)

- Project: `ray-project/ray`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: good first issue; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [\[Data\] Feature request: row-level filename control in write APIs (migration path from `get_filename_for_row()`)](https://github.com/ray-project/ray/issues/64032)

- Project: `ray-project/ray`
- Tier: `triage-lead`
- Evidence: Documentation-related issue with no assignee listed
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Data\] Infinite recursion in ansitowin32.py (under tqdm_ray)](https://github.com/ray-project/ray/issues/51337)

- Project: `ray-project/ray`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Data\] Support integration with Apache Celeborn](https://github.com/ray-project/ray/issues/58687)

- Project: `ray-project/ray`
- Tier: `triage-lead`
- Evidence: Unassigned enhancement with community reactions
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Data\] ray.data.read_delta silently drops columns on Delta tables with column mapping enabled](https://github.com/ray-project/ray/issues/64854)

- Project: `ray-project/ray`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: unexpected blank assistant message after an assistant message with "tool calls"](https://github.com/BerriAI/litellm/issues/31553)

- Project: `BerriAI/litellm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Data\] AutoscalingCoordinator._reallocate_resources is O(R·N²) and holds its lock, starving concurrent datasets at scale (op_budget→0)](https://github.com/ray-project/ray/issues/63924)

- Project: `ray-project/ray`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Umbrella\] Ray Sandboxing with gVisor](https://github.com/ray-project/ray/issues/65352)

- Project: `ray-project/ray`
- Tier: `triage-lead`
- Evidence: Unassigned enhancement with community reactions
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: Host-memory leak on eager `reshape_and_cache_flash` path](https://github.com/vllm-project/vllm/issues/50150)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: mnnvl allreduce workspace init hangs 30s and leaks GPU memory on IB-only multi-node](https://github.com/vllm-project/vllm/issues/51986)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [LiteLLM](https://github.com/BerriAI/litellm)

- **Release** [v1.99.0-dev.1](https://github.com/BerriAI/litellm/releases/tag/v1.99.0-dev.1) — 
- **Issue** [\[Feature\]: Native NeuralTrust TrustGuard guardrail](https://github.com/BerriAI/litellm/issues/37459) — 0 comments · 10 reactions · open
- **Pull Request** [feat(rate-limiting): tag-scoped token/request/dollar/concurrency rate limits](https://github.com/BerriAI/litellm/pull/36541) — 92 comments · 1 reactions · open
- **Pull Request** [feat(auto-router)!: scope shadow eval jobs to multiple keys](https://github.com/BerriAI/litellm/pull/37251) — 54 comments · 1 reactions · closed
- **Pull Request** [feat(ui): multi-key shadow eval picker and per-key breakdown](https://github.com/BerriAI/litellm/pull/37389) — 39 comments · 1 reactions · open
- **Pull Request** [feat(cost): support time-based off-peak pricing in cost calculation](https://github.com/BerriAI/litellm/pull/31725) — 24 comments · 4 reactions · open
- **Pull Request** [feat(mcp): add admin-declared per-user fields for MCP servers](https://github.com/BerriAI/litellm/pull/28218) — 35 comments · 1 reactions · closed
- **Pull Request** [feat(ui): pick the auto router's custom classifier from a config-declared registry](https://github.com/BerriAI/litellm/pull/37374) — 33 comments · 1 reactions · closed
- **Pull Request** [feat(observability): expose per-pod request pressure and the enforced concurrency ceiling](https://github.com/BerriAI/litellm/pull/36639) — 31 comments · 1 reactions · open
- **Pull Request** [fix(streaming): backfill response.completed output from output_item.done events](https://github.com/BerriAI/litellm/pull/31332) — 20 comments · 3 reactions · open
- **Pull Request** [feat(observability): expose Prisma connection pool saturation metrics](https://github.com/BerriAI/litellm/pull/36607) — 28 comments · 1 reactions · open
- **Pull Request** [feat(observability): expose scheduled background job and cron lock telemetry](https://github.com/BerriAI/litellm/pull/36636) — 24 comments · 1 reactions · open
- **Pull Request** [fix(bedrock): Filter anthropic-beta header for Bedrock passthrough](https://github.com/BerriAI/litellm/pull/20012) — 10 comments · 5 reactions · open
- **Pull Request** [feat(guardrails): add Lakera v2 skip-message honoring and advisory (inject_system_message) mode](https://github.com/BerriAI/litellm/pull/34940) — 22 comments · 1 reactions · open
- **Pull Request** [feat(otel): attribute Prisma database spans to PostgreSQL instead of localhost](https://github.com/BerriAI/litellm/pull/36595) — 23 comments · 1 reactions · closed
- **Pull Request** [feat(search): add Amazon Bedrock AgentCore web search provider](https://github.com/BerriAI/litellm/pull/36331) — 20 comments · 1 reactions · closed
- **Pull Request** [fix: omit thinking.type=disabled for always-on thinking Claude models](https://github.com/BerriAI/litellm/pull/37510) — 24 comments · 1 reactions · open
- **Issue** [\[Bug\]:  Vertex AI: Do not enforce credentials when using global api endpoint/vertex express token](https://github.com/BerriAI/litellm/issues/21036) — 3 comments · 4 reactions · closed
- **Issue** [\[Feature\]: Add Huawei Cloud ModelArts MaaS as a new LLM provider"](https://github.com/BerriAI/litellm/issues/27860) — 1 comments · 4 reactions · closed
- **Issue** [\[Feature\]: Add Amazon Bedrock AgentCore Web Search as a native search provider (search_tools / websearch_interception backend)](https://github.com/BerriAI/litellm/issues/31819) — 5 comments · 2 reactions · closed
- **Issue** [\[Bug\]: Anthropic message transformer always sets effort level to xhigh on all claude models which results in invalid request error](https://github.com/BerriAI/litellm/issues/27168) — 2 comments · 3 reactions · closed
- **Pull Request** [prototype(ui): per-user fields for MCP servers (mock/throwaway)](https://github.com/BerriAI/litellm/pull/28219) — 14 comments · 1 reactions · closed
- **Pull Request** [perf(streaming): add shared JSONFragmentAccumulator for Vertex and Anthropic](https://github.com/BerriAI/litellm/pull/36610) — 15 comments · 1 reactions · open
- **Pull Request** [feat(logging): add async_post_call_failure_deployment_hook](https://github.com/BerriAI/litellm/pull/36657) — 15 comments · 1 reactions · open
- **Pull Request** [feat(rust): route /chat/completions through the Rust core for anthropic and bedrock](https://github.com/BerriAI/litellm/pull/37241) — 15 comments · 1 reactions · open
- **Pull Request** [fix(otel): route Phoenix traces to per-key/team projects under otel v2](https://github.com/BerriAI/litellm/pull/36706) — 12 comments · 1 reactions · open
- **Pull Request** [feat(proxy): enqueued-token rate limiting for batches with refund on completion and cancellation](https://github.com/BerriAI/litellm/pull/37539) — 17 comments · 1 reactions · open
- **Issue** [\[Feature\]: Pass immutable safety identifiers (user_ids) by default](https://github.com/BerriAI/litellm/issues/14505) — 2 comments · 2 reactions · open
- **Issue** [\[Bug\]: Can't login despite setting password](https://github.com/BerriAI/litellm/issues/23451) — 6 comments · 1 reactions · open
- **Pull Request** [fix(bedrock): add missing type field in parallel_tool_calls tool_choi…](https://github.com/BerriAI/litellm/pull/22638) — 6 comments · 3 reactions · open

### [vLLM](https://github.com/vllm-project/vllm)

- **Issue** [\[Bug\]: MTP speculative decoding crash with illegal memory access on long sequences (Qwen3.6-27B-FP8, v0.19.1)](https://github.com/vllm-project/vllm/issues/40756) — 41 comments · 16 reactions · open
- **Pull Request** [\[Spec Decode\] DFlash2: local convolution + candidate selector](https://github.com/vllm-project/vllm/pull/52816) — 21 comments · 36 reactions · open
- **Pull Request** [\[6/N\]\[KV-Cache Layout Refactor\] Standardize KV cache layout](https://github.com/vllm-project/vllm/pull/51718) — 36 comments · 2 reactions · open
- **Pull Request** [\[Core\]\[V1\] Support trace_decode_token_ids for deterministic decode replay](https://github.com/vllm-project/vllm/pull/46701) — 31 comments · 3 reactions · open
- **Pull Request** [\[Bugfix\]\[Core\]\[Model\] Voxtral realtime: fix boot-OOM / silent-hang / max-len crash on 16 GiB](https://github.com/vllm-project/vllm/pull/45022) — 19 comments · 3 reactions · open
- **Pull Request** [\[Feature\]\[Whisper\] Native word-level timestamps (cross-attention + DTW)](https://github.com/vllm-project/vllm/pull/47664) — 12 comments · 9 reactions · open
- **Pull Request** [\[Bugfix\] Support MistralCommonBackend tokenizers in the xgrammar structured-output backend](https://github.com/vllm-project/vllm/pull/52720) — 35 comments · 2 reactions · open
- **Pull Request** [\[Perf\]\[Kernel\] Fused DSA indexer Top-k kernel (LiteTopk)](https://github.com/vllm-project/vllm/pull/48726) — 8 comments · 2 reactions · open
- **Pull Request** [\[ROCm\] DeepSeek-V4-Pro PD Disaggregation through MORI IO KV Connector on AMD GPUs](https://github.com/vllm-project/vllm/pull/48989) — 9 comments · 2 reactions · open
- **Pull Request** [\[ModelRunner V2\] Speculative Decoding NGram GPU Implementations](https://github.com/vllm-project/vllm/pull/40704) — 26 comments · 3 reactions · open
- **Pull Request** [\[Spec Decode\] Add D-cut: Adaptive Verification Depth Pruning for Batched Speculative Decoding](https://github.com/vllm-project/vllm/pull/47131) — 6 comments · 9 reactions · open
- **Pull Request** [\[Performance\] Add Triton kernel for Gemma3n sparse GELU](https://github.com/vllm-project/vllm/pull/48498) — 6 comments · 2 reactions · open
- **Pull Request** [\[Kernel\]\[Model\] Add manual CUDA RoPE KV-cache fusion for Llama](https://github.com/vllm-project/vllm/pull/52363) — 6 comments · 2 reactions · open
- **Pull Request** [\[Formatting\] Collapse multi-line arg lists where possible](https://github.com/vllm-project/vllm/pull/43449) — 5 comments · 2 reactions · open
- **Pull Request** [Enable return_routed_experts support with CPU KV offload](https://github.com/vllm-project/vllm/pull/45635) — 25 comments · 3 reactions · open
- **Pull Request** [\[Feature\] NVFP4 dispatch for fused RoPE quantization](https://github.com/vllm-project/vllm/pull/46031) — 4 comments · 3 reactions · open
- **Pull Request** [Dynamic-fork scheduling, Medusa/MTP spec decode, and InternVL resize for HPD-Parsing (based on v0.17.1)](https://github.com/vllm-project/vllm/pull/48715) — 2 comments · 3 reactions · open
- **Pull Request** [\[Frontend\]\[Core\]\[Spec Decode\] Per-request acceptance stats in OpenAI API responses](https://github.com/vllm-project/vllm/pull/48915) — 26 comments · 2 reactions · open
- **Pull Request** [\[ROCm\]: Bump triton 3.7 commit](https://github.com/vllm-project/vllm/pull/52819) — 21 comments · 3 reactions · closed
- **Pull Request** [\[Core\] feat: add optional cap for --max-model-len auto](https://github.com/vllm-project/vllm/pull/41391) — 15 comments · 4 reactions · open
- **Pull Request** [\[Examples\] Add Ray Data batch VLM inference example with ROCm support](https://github.com/vllm-project/vllm/pull/47191) — 3 comments · 2 reactions · open
- **Pull Request** [feat(mxfp4): add MXFP4 expert cache support to DeepSeek V4](https://github.com/vllm-project/vllm/pull/48505) — 3 comments · 2 reactions · open
- **Pull Request** [\[Model\]\[Kimi K3\] Project DSpark aux states before SP all-gather](https://github.com/vllm-project/vllm/pull/50658) — 2 comments · 2 reactions · open
- **Pull Request** [\[Spec Decode\]\[Perf\] Optimize DSpark Markov head with addmm](https://github.com/vllm-project/vllm/pull/50737) — 3 comments · 2 reactions · open
- **Pull Request** [\[KV Connector\] Add decode offloading to Mooncake Store consumers](https://github.com/vllm-project/vllm/pull/52466) — 11 comments · 5 reactions · closed
- **Pull Request** [\[Frontend\]\[Core\]\[Tracing\] Add token-level OTEL tracing for prod observability](https://github.com/vllm-project/vllm/pull/32573) — 17 comments · 4 reactions · open
- **Pull Request** [\[Kernel\] Support UE8M0 scales in fused SiLU block quant](https://github.com/vllm-project/vllm/pull/43399) — 1 comments · 2 reactions · open
- **Pull Request** [\[Kernel\] Add prepared-input fast path with MiniMax-M2 top-k/act quant fusion](https://github.com/vllm-project/vllm/pull/43592) — 1 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\]\[Core\] Reserve the KV null block when validating max_model_len](https://github.com/vllm-project/vllm/pull/47272) — 13 comments · 4 reactions · open
- **Pull Request** [\[Refactor\]: StructuredOutputManager x Speculative Decoding Refactor](https://github.com/vllm-project/vllm/pull/48200) — 8 comments · 5 reactions · open

### [SGLang](https://github.com/sgl-project/sglang)

- **Issue** [\[Roadmap\]: SGLang Distributed KVCache System For Agentic Workload](https://github.com/sgl-project/sglang/issues/21846) — 21 comments · 28 reactions · open
- **Issue** [\[Feature\] NSA optimization roadmap](https://github.com/sgl-project/sglang/issues/11989) — 12 comments · 13 reactions · closed
- **Issue** [\[RFC\] Agent-Aware KV Cache Phase 1 for Agentic Workloads](https://github.com/sgl-project/sglang/issues/24656) — 11 comments · 13 reactions · open
- **Issue** [\[Tracking\] CI Test Failures and Fixes](https://github.com/sgl-project/sglang/issues/17050) — 13 comments · 10 reactions · open
- **Issue** [\[RFC\] Sglang non-GPU process rust migration](https://github.com/sgl-project/sglang/issues/23206) — 8 comments · 11 reactions · open
- **Pull Request** [\[HiCache\] Fix PP inconsistency with HiCache L3 (#22607)](https://github.com/sgl-project/sglang/pull/27010) — 42 comments · 3 reactions · open
- **Pull Request** [\[P/D disagg\] Decode-side radix cache for SWA hybrid models (unified radix tree)](https://github.com/sgl-project/sglang/pull/27770) — 41 comments · 3 reactions · open
- **Pull Request** [\[DSv4\] Integrate TRT-LLM DSv4 Attention for SM100/103](https://github.com/sgl-project/sglang/pull/30805) — 60 comments · 0 reactions · open
- **Pull Request** [\[Model\] Support Ling-3.0-flash (BailingMoeV3)](https://github.com/sgl-project/sglang/pull/33561) — 4 comments · 9 reactions · open
- **Pull Request** [test: switch the Inkling-Small NVFP4 deterministic suite to DSPARK](https://github.com/sgl-project/sglang/pull/35293) — 38 comments · 0 reactions · open
- **Pull Request** [ROCm: Fix AITER attention for Qwen3-Coder-Next hybrid models](https://github.com/sgl-project/sglang/pull/18571) — 34 comments · 1 reactions · closed
- **Issue** [\[AITER-Upgrade\] PR readiness](https://github.com/sgl-project/sglang/issues/21302) — 22 comments · 0 reactions · open
- **Issue** [\[RFC\] KVCR as a HiCacheStorage backend for peer-to-peer KV reuse](https://github.com/sgl-project/sglang/issues/32903) — 1 comments · 6 reactions · open
- **Pull Request** [\[Diffusion\]\[CPU\] Adding AMX optimizations for CPU platform](https://github.com/sgl-project/sglang/pull/30719) — 31 comments · 0 reactions · open
- **Pull Request** [\[AMD\] \[Docker\] Upgrade Python 3.12 + torch 2.11 + triton 3.7 in ROCm 7.2.4](https://github.com/sgl-project/sglang/pull/30984) — 22 comments · 1 reactions · closed
- **Pull Request** [\[MoE Refactor\] Migrate SM100 trtllm-gen mxfp4 MoE onto MoeRunner](https://github.com/sgl-project/sglang/pull/32405) — 20 comments · 1 reactions · open
- **Pull Request** [TP/PP Consensus checker](https://github.com/sgl-project/sglang/pull/34406) — 4 comments · 5 reactions · open
- **Pull Request** [\[NVIDIA\]\[comm\] Merge EP+MoE-TP post-experts all-reduces into one _TP reduction](https://github.com/sgl-project/sglang/pull/32963) — 23 comments · 0 reactions · open
- **Pull Request** [\[NPU\] \[Diffusion\] Support MiniMax H3 on Ascend NPU's](https://github.com/sgl-project/sglang/pull/33569) — 22 comments · 0 reactions · open
- **Pull Request** [\[Spec\] Fix Dspark and Dflash state divergence across TP rank](https://github.com/sgl-project/sglang/pull/33614) — 19 comments · 1 reactions · open
- **Pull Request** [\[PD\] Introduce runtime role switching between prefill and decode](https://github.com/sgl-project/sglang/pull/28403) — 9 comments · 3 reactions · open
- **Pull Request** [feat(diffusion): add OmniDreams autoregressive video world model](https://github.com/sgl-project/sglang/pull/27442) — 15 comments · 1 reactions · open
- **Pull Request** [\[Model\] Add LLaDA2.2 Block Routing MoE support](https://github.com/sgl-project/sglang/pull/31768) — 6 comments · 3 reactions · open
- **Pull Request** [\[XPU\]\[Diffusion\] Enable MiniMax H3 on XPU platforms](https://github.com/sgl-project/sglang/pull/33366) — 19 comments · 0 reactions · open
- **Issue** [\[Feature\] W4A8 MoE kernel for NVFP4 models on non-Blackwell GPUs (SM90)](https://github.com/sgl-project/sglang/issues/22459) — 8 comments · 0 reactions · closed
- **Issue** [\[Bug\] parallel_tool_calls=False is not strictly enforced](https://github.com/sgl-project/sglang/issues/9696) — 9 comments · 0 reactions · closed
- **Pull Request** [\[Mooncake\] Fix silent SSD offload corruption when TP/PP ranks share ssd_offload_path](https://github.com/sgl-project/sglang/pull/31926) — 4 comments · 3 reactions · open
- **Pull Request** [\[RFC\] Rust Tree Core Full Component](https://github.com/sgl-project/sglang/pull/32710) — 5 comments · 3 reactions · open
- **Pull Request** [\[AMD\] Add dense-FP8 for MXFP4 checkpoints with fused silu, mul, activation quant](https://github.com/sgl-project/sglang/pull/28932) — 15 comments · 0 reactions · open
- **Issue** [\[RFC\]\[Refactor\] `mem_cache` pool / allocator restructure](https://github.com/sgl-project/sglang/issues/25371) — 0 comments · 2 reactions · open

### [Ray](https://github.com/ray-project/ray)

- **Issue** [\[Data\] Support integration with Apache Celeborn](https://github.com/ray-project/ray/issues/58687) — 4 comments · 6 reactions · open
- **Issue** [\[Data\] Reduce the memory usage of checkpoint](https://github.com/ray-project/ray/issues/60200) — 4 comments · 4 reactions · open
- **Issue** [\[Data\] Ray Data CBO (Cost-Based Optimizer) Design](https://github.com/ray-project/ray/issues/61477) — 9 comments · 3 reactions · open
- **Issue** [\[Data\] Support predicate pushdown at Delta Lake level](https://github.com/ray-project/ray/issues/61547) — 4 comments · 1 reactions · open
- **Issue** [\[Data\] Refactor: Checkpoint loading from broadcast-join to bucket-join style](https://github.com/ray-project/ray/issues/61509) — 2 comments · 1 reactions · open
- **Issue** [\[Core\]\[GCS\] Export Redis payload byte metrics by command and table](https://github.com/ray-project/ray/issues/65552) — 2 comments · 0 reactions · open
- **Issue** [\[Data\] AutoscalingCoordinator._reallocate_resources is O(R·N²) and holds its lock, starving concurrent datasets at scale (op_budget→0)](https://github.com/ray-project/ray/issues/63924) — 4 comments · 0 reactions · open
- **Issue** [\[Train\] Share PlacementGroupCleaner across concurrent Train v2 runs](https://github.com/ray-project/ray/issues/65443) — 1 comments · 0 reactions · open
- **Issue** [\[Data\] Fused map functions are serialized with every shuffle-map task](https://github.com/ray-project/ray/issues/65479) — 0 comments · 0 reactions · open
- **Issue** [\[Data\] `allow ray_remote_args_fn` to take the sample as argument](https://github.com/ray-project/ray/issues/60452) — 2 comments · 0 reactions · open
- **Issue** [\[Data/Autoscaler\] Proposal: Release all resources of an upstream op at once when it finishes, instead of step-wise scale down](https://github.com/ray-project/ray/issues/63299) — 2 comments · 0 reactions · open
- **Issue** [\[Umbrella\] Ray Sandboxing with gVisor](https://github.com/ray-project/ray/issues/65352) — 10 comments · 3 reactions · open
- **Pull Request** [\[serve\] Columnar zero-copy autoscaling-metrics ingest](https://github.com/ray-project/ray/pull/64281) — 2 comments · 1 reactions · open
- **Issue** [\[Data\] bundle blocks automatically for downstream non-UDF operators](https://github.com/ray-project/ray/issues/59711) — 0 comments · 0 reactions · open
- **Issue** [\[Data\] Optimize triple loop in default_autoscaling_coordinator.py](https://github.com/ray-project/ray/issues/61485) — 0 comments · 0 reactions · open
- **Issue** [\[Data\] Support to read from/ write to hologres in ray](https://github.com/ray-project/ray/issues/62002) — 1 comments · 0 reactions · open
- **Issue** [\[Data\] configure map task memory requirement based on memory profiling](https://github.com/ray-project/ray/issues/62230) — 0 comments · 0 reactions · open
- **Issue** [\[Data\] Support incremental reads for Iceberg tables](https://github.com/ray-project/ray/issues/64464) — 1 comments · 0 reactions · open
- **Pull Request** [feat(dag): support pinned memory for CPU <-> GPU tensor transfers (#48086)](https://github.com/ray-project/ray/pull/65566) — 1 comments · 1 reactions · closed
- **Issue** [\[Umbrella\] Revisit Ray dashboard API status code](https://github.com/ray-project/ray/issues/51442) — 14 comments · 1 reactions · open
- **Pull Request** [\[serve\] Add max_request_retries to bound router retry loops](https://github.com/ray-project/ray/pull/64399) — 16 comments · 2 reactions · open
- **Pull Request** [\[core\]\[sandbox\] Make Ray Sandbox run Docker-built images out of the box](https://github.com/ray-project/ray/pull/65570) — 1 comments · 5 reactions · open
- **Issue** [\[Data\] Infinite recursion in ansitowin32.py (under tqdm_ray)](https://github.com/ray-project/ray/issues/51337) — 7 comments · 2 reactions · open
- **Pull Request** [\[data\]\[llm\] Add vLLM engine metrics and request-latency overhead to single-node batch benchmark](https://github.com/ray-project/ray/pull/63912) — 14 comments · 1 reactions · open
- **Pull Request** [docs(serve): add FunASR ASR integration example](https://github.com/ray-project/ray/pull/64053) — 18 comments · 1 reactions · open
- **Issue** [\[Data\] ray.data.read_delta silently drops columns on Delta tables with column mapping enabled](https://github.com/ray-project/ray/issues/64854) — 8 comments · 0 reactions · open
- **Pull Request** [\[core\] Add opt-in swap accounting to memory monitor and scheduler](https://github.com/ray-project/ray/pull/63793) — 10 comments · 1 reactions · closed
- **Issue** [\[data\] ObjectRefs passed to map UDF are not automatically deref'ed](https://github.com/ray-project/ray/issues/49207) — 1 comments · 2 reactions · open
- **Issue** [\[core\] Unify executor threads when enabling/disabling concurrency_groups](https://github.com/ray-project/ray/issues/54639) — 5 comments · 0 reactions · open
- **Pull Request** [\[Data\] Add checkpoint support for Iceberg read/write](https://github.com/ray-project/ray/pull/61753) — 9 comments · 1 reactions · open

### [BentoML](https://github.com/bentoml/BentoML)

- **Pull Request** [feat: agent skills for deploying BentoML services to Kubernetes and EC2](https://github.com/bentoml/BentoML/pull/5683) — 0 comments · 0 reactions · open
- **Pull Request** [fix: distinguish task cancel OpenAPI operation IDs](https://github.com/bentoml/BentoML/pull/5697) — 0 comments · 0 reactions · open
