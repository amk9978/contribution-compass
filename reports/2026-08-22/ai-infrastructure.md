# AI Infrastructure — 2026-08-22

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [\[Feature\]: support model discovery with custom provider](https://github.com/BerriAI/litellm/issues/20064)

- Project: `BerriAI/litellm`
- Tier: `triage-lead`
- Evidence: Unassigned enhancement with community reactions
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: litellm-non_root cannot run Prisma migrations because @prisma/engines is not writable](https://github.com/BerriAI/litellm/issues/34236)

- Project: `BerriAI/litellm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: Gemini request fails when cache size is too small](https://github.com/BerriAI/litellm/issues/17696)

- Project: `BerriAI/litellm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\] Potential Context State Leakage in MCP Routing (_mcp_active_toolset_id) under Async Stream Interruption](https://github.com/BerriAI/litellm/issues/30416)

- Project: `BerriAI/litellm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[RLlib\] Checkpointing fails with CUDA GPU learner using the new API stack](https://github.com/ray-project/ray/issues/53793)

- Project: `ray-project/ray`
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

### [\[Bug\]: Qwen3.5 122b a10 model RuntimeError: Triton Error \[CUDA\]: an illegal memory access was encountered](https://github.com/vllm-project/vllm/issues/51297)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: OffloadingConnector stores but never serves when MTP/EAGLE speculative decoding is enabled (hybrid GDN model, XPU)](https://github.com/vllm-project/vllm/issues/52735)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [LiteLLM](https://github.com/BerriAI/litellm)

- **Issue** [\[Feature\]: Support GPT-5.6 (Sol / Terra / Luna) via Amazon Bedrock Runtime](https://github.com/BerriAI/litellm/issues/37285) — 0 comments · 18 reactions · closed
- **Issue** [\[Feature\]: support model discovery with custom provider](https://github.com/BerriAI/litellm/issues/20064) — 10 comments · 10 reactions · open
- **Release** [v1.99.0-dev.2](https://github.com/BerriAI/litellm/releases/tag/v1.99.0-dev.2) — 
- **Pull Request** [feat(rate-limiting): tag-scoped token/request/dollar/concurrency rate limits](https://github.com/BerriAI/litellm/pull/36541) — 148 comments · 1 reactions · open
- **Pull Request** [feat(ui): add and delete auto-router tiers with classifier definitions](https://github.com/BerriAI/litellm/pull/37246) — 61 comments · 1 reactions · closed
- **Pull Request** [fix: omit thinking.type=disabled for always-on thinking Claude models](https://github.com/BerriAI/litellm/pull/37510) — 42 comments · 1 reactions · closed
- **Pull Request** [feat(ui): edit the auto-router tier set with custom classifier-defined tiers](https://github.com/BerriAI/litellm/pull/37735) — 51 comments · 1 reactions · open
- **Pull Request** [fix(proxy): make per-model budgets track spend, enforce, and report the same counter](https://github.com/BerriAI/litellm/pull/37736) — 42 comments · 1 reactions · closed
- **Pull Request** [feat(cost): support time-based off-peak pricing in cost calculation](https://github.com/BerriAI/litellm/pull/31725) — 25 comments · 4 reactions · open
- **Issue** [\[Bug\]: /metrics endpoint not allowing for unauthenticated access](https://github.com/BerriAI/litellm/issues/27926) — 3 comments · 7 reactions · closed
- **Pull Request** [feat(newrelic): per-team cost and usage metrics via team callbacks](https://github.com/BerriAI/litellm/pull/37610) — 30 comments · 1 reactions · open
- **Pull Request** [feat(ui): edit the auto-router tier set with custom classifier-defined tiers](https://github.com/BerriAI/litellm/pull/37893) — 34 comments · 1 reactions · open
- **Pull Request** [feat(logging): add async_post_call_failure_deployment_hook](https://github.com/BerriAI/litellm/pull/36657) — 29 comments · 1 reactions · open
- **Pull Request** [fix(proxy): route blocked models through healthy fallbacks](https://github.com/BerriAI/litellm/pull/36672) — 25 comments · 2 reactions · open
- **Issue** [\[Bug\]: litellm-non_root cannot run Prisma migrations because @prisma/engines is not writable](https://github.com/BerriAI/litellm/issues/34236) — 6 comments · 5 reactions · open
- **Pull Request** [feat(router): per-group supported reasoning efforts via model-map intersection](https://github.com/BerriAI/litellm/pull/37732) — 27 comments · 1 reactions · closed
- **Pull Request** [feat(vertex_ai): add Lyria music generation support](https://github.com/BerriAI/litellm/pull/30304) — 24 comments · 1 reactions · open
- **Pull Request** [feat(prometheus): expose team-scoped rate limit gauges](https://github.com/BerriAI/litellm/pull/37215) — 7 comments · 5 reactions · open
- **Pull Request** [feat(newrelic): per-team New Relic trace routing via team callbacks](https://github.com/BerriAI/litellm/pull/37603) — 20 comments · 1 reactions · open
- **Pull Request** [fix(spend): credit prompt caching savings only when the gateway injected the breakpoints](https://github.com/BerriAI/litellm/pull/37760) — 21 comments · 1 reactions · open
- **Issue** [\[Bug\] UI very slow in version 1.82.x](https://github.com/BerriAI/litellm/issues/23005) — 10 comments · 2 reactions · open
- **Issue** [\[Feature\]: Support Anthropic Workload Identity Federation (OIDC JWT-bearer token exchange)](https://github.com/BerriAI/litellm/issues/28607) — 3 comments · 4 reactions · open
- **Issue** [MCP gateway-DCR bridge (oauth_delegate + dcr_bridge): unsealed upstream credential discarded on tool calls, upstream never receives Authorization](https://github.com/BerriAI/litellm/issues/36358) — 2 comments · 4 reactions · open
- **Pull Request** [fix(helm): support authenticated ServiceMonitor scrapes](https://github.com/BerriAI/litellm/pull/30565) — 18 comments · 1 reactions · open
- **Pull Request** [perf(streaming): add shared JSONFragmentAccumulator for Vertex and Anthropic](https://github.com/BerriAI/litellm/pull/36610) — 19 comments · 1 reactions · open
- **Pull Request** [feat(ui): add per-key Savings tab to key detail page](https://github.com/BerriAI/litellm/pull/37693) — 19 comments · 1 reactions · closed
- **Pull Request** [feat(proxy): add router_model_name to auto-routed response bodies](https://github.com/BerriAI/litellm/pull/37725) — 18 comments · 1 reactions · closed
- **Pull Request** [fix(cost): bill Azure Foundry GPT-5.6 prompt cache writes](https://github.com/BerriAI/litellm/pull/35125) — 13 comments · 2 reactions · open
- **Issue** [\[Bug\]: Usage Dashboard: Two Issues with Spend Reporting and Failed Request Attribution](https://github.com/BerriAI/litellm/issues/11929) — 15 comments · 0 reactions · open
- **Issue** [\[Bug\]: Gemini request fails when cache size is too small](https://github.com/BerriAI/litellm/issues/17696) — 6 comments · 2 reactions · open

### [vLLM](https://github.com/vllm-project/vllm)

- **Issue** [\[Feature\]: DeepSeek-V4 Flash sm_80 (A100/A800) support](https://github.com/vllm-project/vllm/issues/40851) — 45 comments · 30 reactions · open
- **Pull Request** [\[Spec Decode\] DFlash2: local convolution + candidate selector](https://github.com/vllm-project/vllm/pull/52816) — 49 comments · 52 reactions · closed
- **Pull Request** [\[Core\] Extensible (growable) KV cache](https://github.com/vllm-project/vllm/pull/50779) — 38 comments · 5 reactions · open
- **Pull Request** [\[6/N\]\[KV-Cache Layout Refactor\] Standardize KV cache layout](https://github.com/vllm-project/vllm/pull/51718) — 80 comments · 2 reactions · closed
- **Issue** [\[Feature\]: Implement `TRITON_MLA_SPARSE` backend for sm80/120/121 support of Sparse MLA](https://github.com/vllm-project/vllm/issues/38006) — 14 comments · 10 reactions · open
- **Pull Request** [\[Kernel\] FlashInfer CuTe-DSL NVFP4 Quantization](https://github.com/vllm-project/vllm/pull/49775) — 17 comments · 3 reactions · open
- **Pull Request** [Add routed expert loading for gpt-oss](https://github.com/vllm-project/vllm/pull/52209) — 21 comments · 2 reactions · open
- **Pull Request** [\[Kernel\]\[ROCm\] Cover OCP MX MoE emulation in the mxfp4 oracle test](https://github.com/vllm-project/vllm/pull/43983) — 18 comments · 2 reactions · open
- **Pull Request** [\[K3 Perf\] Fuse MXFP4 top-k finalization into latent-tail, ~5% E2E latency reduction](https://github.com/vllm-project/vllm/pull/53152) — 13 comments · 3 reactions · closed
- **Pull Request** [\[MoE\] Generalize masked activation for padded layouts](https://github.com/vllm-project/vllm/pull/51217) — 14 comments · 2 reactions · open
- **Pull Request** [\[Performance\]\[MLA\] Use FP16 logits for sparse indexer](https://github.com/vllm-project/vllm/pull/52696) — 15 comments · 2 reactions · open
- **Pull Request** [\[ROCm\] DeepSeek-V4-Pro PD Disaggregation through MORI IO KV Connector on AMD GPUs](https://github.com/vllm-project/vllm/pull/48989) — 10 comments · 2 reactions · open
- **Pull Request** [\[Core\]\[MRV2\] Support eagle3 spec decode with pipeline parallel](https://github.com/vllm-project/vllm/pull/50514) — 35 comments · 2 reactions · open
- **Pull Request** [\[ROCm\]\[Perf\] Optimize DeepSeek V4 C4A top-k with AITER](https://github.com/vllm-project/vllm/pull/52882) — 11 comments · 2 reactions · closed
- **Pull Request** [\[Bugfix\] Fix MiniMax M3 prompt reasoning initialization](https://github.com/vllm-project/vllm/pull/50594) — 33 comments · 2 reactions · open
- **Pull Request** [\[ModelOpt\] Redesign the LinearMethod classes using the generic QuantKey-driven method](https://github.com/vllm-project/vllm/pull/49381) — 31 comments · 2 reactions · open
- **Pull Request** [\[Perf\] Support internal prefill checkpoints for Mamba prefix caching, 9%~25% TTFT improvement](https://github.com/vllm-project/vllm/pull/52789) — 22 comments · 4 reactions · open
- **Pull Request** [\[Feature\] Add batch invariance support to GDN_ATTN backend](https://github.com/vllm-project/vllm/pull/45819) — 16 comments · 6 reactions · open
- **Pull Request** [\[ROCm\]\[Perf\] Avoid extra reshape kernel in Qwen GDN output projection](https://github.com/vllm-project/vllm/pull/47842) — 5 comments · 2 reactions · open
- **Pull Request** [\[Model\]\[MoE\] DeepSeek-V4: add opt-in FlashInfer moe_ep expert backend](https://github.com/vllm-project/vllm/pull/49636) — 24 comments · 3 reactions · open
- **Pull Request** [\[Bugfix\] Fix multi-turn benchmark's sleep to match the configured request rate](https://github.com/vllm-project/vllm/pull/43212) — 3 comments · 3 reactions · open
- **Pull Request** [\[RL\] P2P RDT weight sync](https://github.com/vllm-project/vllm/pull/43375) — 23 comments · 3 reactions · open
- **Pull Request** [\[Bugfix\] Reload speculative draft weights after Level 2 sleep wake](https://github.com/vllm-project/vllm/pull/52487) — 25 comments · 2 reactions · open
- **Pull Request** [\[Pooling\] Report input throughput for batched requests](https://github.com/vllm-project/vllm/pull/53213) — 5 comments · 2 reactions · open
- **Pull Request** [\[Misc\] Add --max-duration-sec to benchmark_serving_multi_turn.py](https://github.com/vllm-project/vllm/pull/43215) — 2 comments · 2 reactions · open
- **Pull Request** [\[Refactor\]: StructuredOutputManager x Speculative Decoding Refactor](https://github.com/vllm-project/vllm/pull/48200) — 11 comments · 5 reactions · open
- **Pull Request** [\[4/N\] HiSparse: host-resident sparse-MLA decode hot-buffering](https://github.com/vllm-project/vllm/pull/51323) — 22 comments · 2 reactions · open
- **Pull Request** [\[Kernel\]\[MoE\] Optimize batched_moe_align_block_size with cooperative writes](https://github.com/vllm-project/vllm/pull/53280) — 2 comments · 2 reactions · open
- **Pull Request** [\[Distributed\] Add OfflineState bloom-filter cooperative caching KV connector](https://github.com/vllm-project/vllm/pull/37066) — 5 comments · 1 reactions · open
- **Pull Request** [\[Bugfix\] fixd issue#37343: prevent TTFT regression by adding batched logprobs budget to scheduler](https://github.com/vllm-project/vllm/pull/37594) — 4 comments · 1 reactions · open

### [SGLang](https://github.com/sgl-project/sglang)

- **Issue** [\[PP + HiCache\] HiCache Consistency Fix Plan](https://github.com/sgl-project/sglang/issues/22607) — 20 comments · 18 reactions · open
- **Issue** [\[Tracking\] CI Test Failures and Fixes](https://github.com/sgl-project/sglang/issues/17050) — 13 comments · 10 reactions · open
- **Release** [v0.5.18](https://github.com/sgl-project/sglang/releases/tag/v0.5.18) — 
- **Pull Request** [\[Model\] Support Ling-3.0-flash (BailingMoeV3)](https://github.com/sgl-project/sglang/pull/33561) — 9 comments · 9 reactions · open
- **Pull Request** [\[DO NOT MERGE\] ci](https://github.com/sgl-project/sglang/pull/35708) — 116 comments · 0 reactions · closed
- **Issue** [\[Roadmap\]Fast Engine Recovery: Weight Cache Daemon](https://github.com/sgl-project/sglang/issues/33522) — 6 comments · 6 reactions · open
- **Pull Request** [fix(test): stabilize nightly precision regression](https://github.com/sgl-project/sglang/pull/34668) — 38 comments · 0 reactions · open
- **Pull Request** [\[DO NOT MERGE\]\[Test\] Tighten the DCP HiCache KL threshold to 0.005](https://github.com/sgl-project/sglang/pull/35380) — 32 comments · 0 reactions · open
- **Issue** [\[AITER-Upgrade\] PR readiness](https://github.com/sgl-project/sglang/issues/21302) — 23 comments · 0 reactions · open
- **Pull Request** [\[fmha_v2\] perf: use non-interleaved paged KV input for trtllm sm90/120 prefill](https://github.com/sgl-project/sglang/pull/32272) — 3 comments · 0 reactions · open
- **Pull Request** [\[AMD\] Enable gfx1250 Support](https://github.com/sgl-project/sglang/pull/32754) — 22 comments · 1 reactions · open
- **Pull Request** [\[NVIDIA\]\[comm\] Merge EP+MoE-TP post-experts all-reduces into one _TP reduction](https://github.com/sgl-project/sglang/pull/32963) — 24 comments · 0 reactions · open
- **Pull Request** [\[Spec\] Fix Dspark and Dflash state divergence across TP rank](https://github.com/sgl-project/sglang/pull/33614) — 20 comments · 1 reactions · open
- **Pull Request** [\[Unified Cache\]\[Draft POC\]: Add optional external-cache linker mode to Unified Radix Cache](https://github.com/sgl-project/sglang/pull/35687) — 1 comments · 6 reactions · open
- **Pull Request** [\[XPU\]\[Diffusion\] Enable MiniMax H3 on XPU platforms](https://github.com/sgl-project/sglang/pull/33366) — 22 comments · 0 reactions · open
- **Issue** [\[Roadmap\] Hicache NIXL backend](https://github.com/sgl-project/sglang/issues/26693) — 9 comments · 2 reactions · open
- **Pull Request** [\[PD\] Introduce runtime role switching between prefill and decode](https://github.com/sgl-project/sglang/pull/28403) — 9 comments · 3 reactions · open
- **Pull Request** [Rust Tree Core with Full/SWA/Mamba Components](https://github.com/sgl-project/sglang/pull/32710) — 8 comments · 3 reactions · open
- **Pull Request** [\[3/N\] elastic-ep: Recapture decode CUDA graphs after scale-up](https://github.com/sgl-project/sglang/pull/33723) — 21 comments · 0 reactions · open
- **Pull Request** [\[AMD\] GDN linear out-proj fusion](https://github.com/sgl-project/sglang/pull/28655) — 15 comments · 1 reactions · open
- **Pull Request** [\[AMD\] Add dense-FP8 for MXFP4 checkpoints with fused silu, mul, activation quant](https://github.com/sgl-project/sglang/pull/28932) — 18 comments · 0 reactions · open
- **Pull Request** [\[AMD\] Enable unified-KV HiSparse on ROCm for DeepSeek-V4](https://github.com/sgl-project/sglang/pull/29168) — 18 comments · 1 reactions · open
- **Pull Request** [\[Model Loading\] Overlap checkpoint staging with CUDA graph capture during startup](https://github.com/sgl-project/sglang/pull/32017) — 10 comments · 2 reactions · closed
- **Pull Request** [\[AMD\] Fix gfx950 Triton compiler crash on fp8 KV-cache attention](https://github.com/sgl-project/sglang/pull/35428) — 19 comments · 0 reactions · closed
- **Issue** [\[RFC\]\[Refactor\] `mem_cache` pool / allocator restructure](https://github.com/sgl-project/sglang/issues/25371) — 0 comments · 2 reactions · open
- **Issue** [\[Bug\] PrefillDelayer can enter a persistent mixed-state feedback loop and collapse prefill progress under DP Attention + chunked prefill](https://github.com/sgl-project/sglang/issues/35241) — 8 comments · 0 reactions · open
- **Issue** [\[Bug\] Qwen3-VL vision features diverge from Transformers/vLLM in v0.5.17 on fine-grained grounding](https://github.com/sgl-project/sglang/issues/35772) — 1 comments · 2 reactions · open
- **Pull Request** [XPU: Enable GLM5.1 (GlmMoeDsaForCausalLM) DSA Attention](https://github.com/sgl-project/sglang/pull/24959) — 12 comments · 1 reactions · open
- **Pull Request** [\[Mooncake\] Fix silent SSD offload corruption when TP/PP ranks share ssd_offload_path](https://github.com/sgl-project/sglang/pull/31926) — 4 comments · 3 reactions · open
- **Pull Request** [\[Spec\] Windowed draft-decode attention for built-in EAGLE / MTP drafts](https://github.com/sgl-project/sglang/pull/32673) — 12 comments · 1 reactions · open

### [Ray](https://github.com/ray-project/ray)

- **Issue** [\[Core\]\[Data\]\[CoreWorker\]Discussion: remaining gRPC thread amplification with many task workers per node](https://github.com/ray-project/ray/issues/64834) — 16 comments · 1 reactions · open
- **Issue** [Supporting Host Name routing rather than primarily relying on IP address/port](https://github.com/ray-project/ray/issues/61651) — 3 comments · 3 reactions · open
- **Issue** [\[Core\] Actor RSS does not drop even if all object refs are released](https://github.com/ray-project/ray/issues/53261) — 9 comments · 0 reactions · open
- **Issue** [\[Data\] AutoscalingCoordinator._reallocate_resources is O(R·N²) and holds its lock, starving concurrent datasets at scale (op_budget→0)](https://github.com/ray-project/ray/issues/63924) — 5 comments · 0 reactions · open
- **Issue** [\[Data\] Fused map functions are serialized with every shuffle-map task](https://github.com/ray-project/ray/issues/65479) — 0 comments · 0 reactions · closed
- **Issue** [\[Rllib\] new API stack uses >2X VRAM of old stack](https://github.com/ray-project/ray/issues/58679) — 2 comments · 0 reactions · open
- **Issue** [RDT: Enable ray.put from a non ray actor](https://github.com/ray-project/ray/issues/64714) — 3 comments · 0 reactions · closed
- **Issue** [\[Umbrella\] Ray Sandboxing with gVisor](https://github.com/ray-project/ray/issues/65352) — 11 comments · 3 reactions · open
- **Pull Request** [\[serve\] Columnar zero-copy autoscaling-metrics ingest](https://github.com/ray-project/ray/pull/64281) — 2 comments · 1 reactions · open
- **Issue** [\[Data\] MCAPDatasource: support file-level packed output to enable shuffle-free episode aggregation](https://github.com/ray-project/ray/issues/65640) — 0 comments · 0 reactions · open
- **Issue** [\[Data\] MCAPDatasource: batched (streaming) message reads to reduce peak memory and enable intra-file pipelining](https://github.com/ray-project/ray/issues/65641) — 0 comments · 0 reactions · open
- **Pull Request** [\[serve\] Router: sticky latency-adaptive queue-length probe deadline (F)](https://github.com/ray-project/ray/pull/64700) — 2 comments · 1 reactions · open
- **Pull Request** [Bump js-yaml from 4.1.0 to 4.3.1 in /python/ray/dashboard/client](https://github.com/ray-project/ray/pull/65281) — 1 comments · 0 reactions · open
- **Pull Request** [Introducing Hostname Resolution for Nodes](https://github.com/ray-project/ray/pull/64350) — 2 comments · 4 reactions · open
- **Issue** [\[Core\]\[Feature request\] Promote `actor_handle._actor_id` to public API](https://github.com/ray-project/ray/issues/32638) — 11 comments · 0 reactions · open
- **Pull Request** [\[data\] Add orc datasource for V2](https://github.com/ray-project/ray/pull/64540) — 8 comments · 1 reactions · open
- **Pull Request** [\[core\]\[joblib\] Add opt-in autoscaling to ray.util.multiprocessing.Pool](https://github.com/ray-project/ray/pull/64957) — 9 comments · 1 reactions · open
- **Pull Request** [\[doc\]\[KubeRay\] Add mTLS for RayClusters user guide](https://github.com/ray-project/ray/pull/65107) — 9 comments · 1 reactions · open
- **Pull Request** [\[Dashboard\] Recover lost GCS node subscriptions](https://github.com/ray-project/ray/pull/63041) — 7 comments · 2 reactions · open
- **Pull Request** [\[dashboard\] Configurable defaults + UI dialogs for py-spy/memray profiling params](https://github.com/ray-project/ray/pull/64806) — 7 comments · 1 reactions · closed
- **Pull Request** [\[core\] feat(rdt): enable driver-side ray.put with NIXL tensor transport](https://github.com/ray-project/ray/pull/65072) — 6 comments · 1 reactions · closed
- **Issue** [\[RLlib\] Checkpointing fails with CUDA GPU learner using the new API stack](https://github.com/ray-project/ray/issues/53793) — 5 comments · 0 reactions · open
- **Issue** [\[Core\]\[KubeRay\] Autoscaler sends all log records, including INFO, to stderr](https://github.com/ray-project/ray/issues/65454) — 0 comments · 0 reactions · closed
- **Issue** [\[Data\] Support refreshing vended-credentials for native catalog Iceberg path](https://github.com/ray-project/ray/issues/65581) — 1 comments · 0 reactions · open
- **Issue** [\[RLlib\] `Checkpointable.from_checkpoint` should have return type `typing.Self` instead of `Checkpointable`](https://github.com/ray-project/ray/issues/65610) — 1 comments · 0 reactions · open
- **Issue** [\[Data\] Make BigQuery (GCP) client construction injectable in read_bigquery / write_bigquery](https://github.com/ray-project/ray/issues/65614) — 1 comments · 0 reactions · open
- **Pull Request** [\[Data\] Decouple sub-progress metrics from progress bar implementations](https://github.com/ray-project/ray/pull/63195) — 4 comments · 1 reactions · open
- **Pull Request** [\[TPU\] Add PyTorch TPU environment variable and runtime_env APIs to Slice and Subslice placement groups](https://github.com/ray-project/ray/pull/65221) — 4 comments · 1 reactions · open
- **Pull Request** [\[llm\]\[ci\] Upgrade to vllm 0.27.0](https://github.com/ray-project/ray/pull/65351) — 5 comments · 1 reactions · open
- **Pull Request** [fix(autoscaler): deduplicate cloud instances during termination](https://github.com/ray-project/ray/pull/65419) — 0 comments · 2 reactions · open

### [BentoML](https://github.com/bentoml/BentoML)

- **Pull Request** [fix: Windows tar symlink extraction and fastai CI dependency resolution](https://github.com/bentoml/BentoML/pull/5689) — 0 comments · 0 reactions · closed
- **Pull Request** [chore(deps): bump actions/checkout from 6 to 7](https://github.com/bentoml/BentoML/pull/5640) — 0 comments · 0 reactions · open
