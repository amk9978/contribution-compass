# AI Infrastructure — 2026-08-14

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [\[Roadmap\] sglang auto tuner](https://github.com/sgl-project/sglang/issues/13363)

- Project: `sgl-project/sglang`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: good first issue; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [\[RFC\]: Support ViT Full CUDA Graph (Tracker)](https://github.com/vllm-project/vllm/issues/38175)

- Project: `vllm-project/vllm`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: help wanted; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [LiteLLM Stability Sprint Roadmap](https://github.com/BerriAI/litellm/issues/30484)

- Project: `BerriAI/litellm`
- Tier: `triage-lead`
- Evidence: Unassigned enhancement with community reactions
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Feature\]: support model discovery with custom provider](https://github.com/BerriAI/litellm/issues/20064)

- Project: `BerriAI/litellm`
- Tier: `triage-lead`
- Evidence: Unassigned enhancement with community reactions
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: KV block corruption in base scheduler, Non-deterministic output at temperature=0 without prefix caching](https://github.com/vllm-project/vllm/issues/39146)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: Garbled Output in DeepSeek-V4 with CUDA Graph Enabled Under Concurrent Identical Input Requests](https://github.com/vllm-project/vllm/issues/41331)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\] DeepSeekV4-Flash produces incorrect output with inline system messages after PR #46025 when `preserved in-place`](https://github.com/vllm-project/vllm/issues/46710)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [LiteLLM](https://github.com/BerriAI/litellm)

- **Issue** [LiteLLM Stability Sprint Roadmap](https://github.com/BerriAI/litellm/issues/30484) — 25 comments · 9 reactions · open
- **Issue** [\[Feature\]: support model discovery with custom provider](https://github.com/BerriAI/litellm/issues/20064) — 9 comments · 10 reactions · open
- **Issue** [\[Feature\]: Auto-populate max_input_tokens/max_output_tokens for hosted vLLM/OpenAI-like models](https://github.com/BerriAI/litellm/issues/27830) — 2 comments · 6 reactions · open
- **Issue** [\[Bug\]: Function tools fail with reasoning_effort error for OpenAI gpt-5.6 family models (gpt-5.6-sol/luna/terra) on /chat/completions](https://github.com/BerriAI/litellm/issues/33221) — 10 comments · 3 reactions · closed
- **Pull Request** [feat(cost): support time-based off-peak pricing in cost calculation](https://github.com/BerriAI/litellm/pull/31725) — 18 comments · 2 reactions · open
- **Pull Request** [feat(rate-limiting): tag-scoped token/request/dollar/concurrency rate limits](https://github.com/BerriAI/litellm/pull/36541) — 27 comments · 1 reactions · open
- **Pull Request** [feat(proxy): serve Anthropic-native /v1/models for Claude Code gateway discovery](https://github.com/BerriAI/litellm/pull/35455) — 7 comments · 4 reactions · closed
- **Pull Request** [feat(ui): manage admin-owned logging destinations](https://github.com/BerriAI/litellm/pull/35517) — 18 comments · 1 reactions · open
- **Issue** [\[Feature\]: Support Azure AI Foundry Agents v2 (Responses API with agent_reference)](https://github.com/BerriAI/litellm/issues/25372) — 4 comments · 3 reactions · open
- **Pull Request** [feat(guardrails): add Lakera v2 skip-message honoring and advisory (inject_system_message) mode](https://github.com/BerriAI/litellm/pull/34940) — 21 comments · 1 reactions · open
- **Pull Request** [feat(proxy): add project-level ITPM and OTPM quotas](https://github.com/BerriAI/litellm/pull/35110) — 21 comments · 1 reactions · open
- **Issue** [\[Bug\]: 400: \[ERROR: Bad Request\] when using image generation from OpenWeb UI](https://github.com/BerriAI/litellm/issues/30300) — 2 comments · 2 reactions · open
- **Pull Request** [fix: replace Redis+in-memory temp MCP server caching with DB-backed draft servers](https://github.com/BerriAI/litellm/pull/32260) — 10 comments · 1 reactions · open
- **Pull Request** [feat(logging): add async_post_call_failure_deployment_hook](https://github.com/BerriAI/litellm/pull/36657) — 10 comments · 1 reactions · open
- **Pull Request** [fix(otel): route Phoenix traces to per-key/team projects under otel v2](https://github.com/BerriAI/litellm/pull/36706) — 10 comments · 1 reactions · open
- **Pull Request** [fix(langfuse): source the emitted metadata blob from StandardLoggingPayload](https://github.com/BerriAI/litellm/pull/36744) — 10 comments · 1 reactions · closed
- **Pull Request** [fix(access groups): sync assigned_team_ids from the team write paths](https://github.com/BerriAI/litellm/pull/36825) — 11 comments · 1 reactions · closed
- **Pull Request** [feat(mcp): clear and reauthorize a server's stored MCP OAuth tokens](https://github.com/BerriAI/litellm/pull/36831) — 10 comments · 1 reactions · open
- **Issue** [\[Feature\]: Add support for Fireworks AI models in Azure Foundry](https://github.com/BerriAI/litellm/issues/26618) — 4 comments · 0 reactions · closed
- **Pull Request** [VLLM: Prevent side-channel attacks via cache salting (CVE-2025-46570)](https://github.com/BerriAI/litellm/pull/27925) — 9 comments · 1 reactions · open
- **Pull Request** [fix(mcp): include server_name and alias in /v1/mcp/server/health response](https://github.com/BerriAI/litellm/pull/32476) — 8 comments · 1 reactions · open
- **Pull Request** [fix(datadog_llm_obs): map tool_calls to DD Message schema and cache tokens to span metrics](https://github.com/BerriAI/litellm/pull/35946) — 8 comments · 1 reactions · open
- **Pull Request** [feat(parallel_ai): add chat + responses LLM provider and full search param support](https://github.com/BerriAI/litellm/pull/36704) — 8 comments · 1 reactions · open
- **Pull Request** [feat(langfuse): migrate the sdk callback to langfuse v4](https://github.com/BerriAI/litellm/pull/36741) — 9 comments · 1 reactions · open
- **Pull Request** [fix(azure): rename max_tokens to max_completion_tokens for gpt-5-chat deployments](https://github.com/BerriAI/litellm/pull/36857) — 8 comments · 1 reactions · open
- **Pull Request** [fix(langfuse): restrict trace steering keys to real langfuse trace fields](https://github.com/BerriAI/litellm/pull/36862) — 8 comments · 1 reactions · open
- **Pull Request** [fix(gemini): map Gemini 3.7 Flash minimal thinking to low](https://github.com/BerriAI/litellm/pull/36874) — 4 comments · 2 reactions · open
- **Issue** [\[Bug\]: Prisma query engine crashes immediately on first query on Windows (pip install) - LiteLLM 1.82.x / 1.83.0](https://github.com/BerriAI/litellm/issues/25260) — 7 comments · 0 reactions · open
- **Issue** [Mid-conversation system-role hoist invalidates the entire prompt-cache prefix (AnthropicMessagesConfig)](https://github.com/BerriAI/litellm/issues/36559) — 3 comments · 0 reactions · open
- **Pull Request** [fix: drop effort parameter for Haiku with azure_ai provider](https://github.com/BerriAI/litellm/pull/31188) — 6 comments · 1 reactions · open

### [vLLM](https://github.com/vllm-project/vllm)

- **Pull Request** [\[MoE\]\[Offload\] Run MoE models exceeding VRAM via expert CPU offloading with GPU cache (--moe-expert-cache-size)](https://github.com/vllm-project/vllm/pull/37190) — 57 comments · 15 reactions · open
- **Pull Request** [Add Muse Glimmer model support](https://github.com/vllm-project/vllm/pull/51655) — 37 comments · 16 reactions · closed
- **Issue** [\[Performance\]: Deepseek-V4 Support and Optimization on ROCm Backend](https://github.com/vllm-project/vllm/issues/41820) — 17 comments · 7 reactions · open
- **Pull Request** [\[Core\] Extensible (growable) KV cache](https://github.com/vllm-project/vllm/pull/50779) — 22 comments · 5 reactions · open
- **Pull Request** [refactor(envs): migrate vllm/envs.py to pydantic-settings](https://github.com/vllm-project/vllm/pull/42136) — 29 comments · 3 reactions · open
- **Pull Request** [Fused BMM+FP8 quant Triton kernel for MLA _v_up_proj (forward_mqa path)](https://github.com/vllm-project/vllm/pull/36297) — 36 comments · 1 reactions · open
- **Pull Request** [\[Core\]\[V1\] Support trace_decode_token_ids for deterministic decode replay](https://github.com/vllm-project/vllm/pull/46701) — 22 comments · 3 reactions · open
- **Pull Request** [\[Attention\]\[MLA\] FlashMLA sparse: DCP on the fp8_ds_mla mixed-batch path + MTP](https://github.com/vllm-project/vllm/pull/46514) — 50 comments · 3 reactions · open
- **Pull Request** [\[Spec Decode\]\[CUDA Graphs\] Enables Eagle drafter support for FULL CUDA Graph mode](https://github.com/vllm-project/vllm/pull/34880) — 49 comments · 2 reactions · closed
- **Pull Request** [\[Core\]\[WIP\] Check for GPU<->CPU sync during CI](https://github.com/vllm-project/vllm/pull/43107) — 29 comments · 3 reactions · open
- **Pull Request** [\[Model\]\[Spec Decode\] Tap the pre-norm AttnRes mixture as the Kimi K3 DFlash aux state](https://github.com/vllm-project/vllm/pull/50487) — 29 comments · 3 reactions · closed
- **Issue** [\[RFC\]: Support ViT Full CUDA Graph (Tracker)](https://github.com/vllm-project/vllm/issues/38175) — 27 comments · 1 reactions · open
- **Pull Request** [\[WIP\]\[Feature\] A new 2-bit KV cache quantisation backend that cuts 5x memory than FP16 (Oscar-2)](https://github.com/vllm-project/vllm/pull/46774) — 23 comments · 5 reactions · open
- **Pull Request** [\[Attention\] TRITON_MLA_SPARSE backend for SM80/SM121 sparse MLA (rebase & takeover of #38476)](https://github.com/vllm-project/vllm/pull/47629) — 22 comments · 5 reactions · open
- **Pull Request** [\[Bugfix\]\[CI\] Retry cached HF tokenizer load after transport failures](https://github.com/vllm-project/vllm/pull/44820) — 8 comments · 2 reactions · open
- **Pull Request** [\[Perf\]\[Kernel\] Fused DSA indexer Top-k kernel (LiteTopk)](https://github.com/vllm-project/vllm/pull/48726) — 8 comments · 2 reactions · open
- **Pull Request** [\[ROCm\] DeepSeek-V4-Pro PD Disaggregation through MORI IO KV Connector on AMD GPUs](https://github.com/vllm-project/vllm/pull/48989) — 8 comments · 2 reactions · open
- **Pull Request** [\[5/N\]\[KV-Cache Layout Refactor\] Backend-published KV packing via customize_spec](https://github.com/vllm-project/vllm/pull/51704) — 29 comments · 2 reactions · closed
- **Issue** [\[Bug\]: KV block corruption in base scheduler, Non-deterministic output at temperature=0 without prefix caching](https://github.com/vllm-project/vllm/issues/39146) — 2 comments · 7 reactions · open
- **Pull Request** [\[ROCm\]\[CI\] Gating more ROCm tests](https://github.com/vllm-project/vllm/pull/44969) — 26 comments · 2 reactions · open
- **Pull Request** [\[ModelRunner v2\] Enable MRV2 for pooling models by default](https://github.com/vllm-project/vllm/pull/48290) — 23 comments · 3 reactions · open
- **Pull Request** [\[K3\] support recoverssm for K3](https://github.com/vllm-project/vllm/pull/51855) — 3 comments · 2 reactions · open
- **Issue** [\[Bug\]: Garbled Output in DeepSeek-V4 with CUDA Graph Enabled Under Concurrent Identical Input Requests](https://github.com/vllm-project/vllm/issues/41331) — 5 comments · 6 reactions · open
- **Pull Request** [Feat/spec decode under pipeline parallel](https://github.com/vllm-project/vllm/pull/50514) — 24 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\] Fix MiniMax M3 prompt reasoning initialization](https://github.com/vllm-project/vllm/pull/50594) — 25 comments · 2 reactions · open
- **Pull Request** [feat: add optional torchembed RoPE backend](https://github.com/vllm-project/vllm/pull/44810) — 2 comments · 2 reactions · open
- **Pull Request** [\[ModelOpt\] Redesign the LinearMethod classes using the generic QuantKey-driven method](https://github.com/vllm-project/vllm/pull/49381) — 22 comments · 2 reactions · open
- **Pull Request** [\[Model\]\[Perf\] Overlap mixed GDN decode and prefill recurrent kernels](https://github.com/vllm-project/vllm/pull/50233) — 3 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\] Fix speculative decoding for short_conv (LFM2) models](https://github.com/vllm-project/vllm/pull/50272) — 18 comments · 4 reactions · open
- **Pull Request** [\[ROCm\]Remove special-case SiTU support model-specific gating](https://github.com/vllm-project/vllm/pull/50597) — 22 comments · 2 reactions · closed

### [SGLang](https://github.com/sgl-project/sglang)

- **Issue** [\[Roadmap\] sglang auto tuner](https://github.com/sgl-project/sglang/issues/13363) — 14 comments · 29 reactions · open
- **Issue** [\[Tracking\] CI Test Failures and Fixes](https://github.com/sgl-project/sglang/issues/17050) — 13 comments · 10 reactions · open
- **Pull Request** [\[P/D disagg\] Decode-side radix cache for SWA hybrid models (unified radix tree)](https://github.com/sgl-project/sglang/pull/27770) — 40 comments · 3 reactions · open
- **Pull Request** [\[HiCache\] Support packed and sidecar draft caches for MTP/EAGLE/DSpark](https://github.com/sgl-project/sglang/pull/30393) — 27 comments · 7 reactions · closed
- **Pull Request** [\[HiCache\] Fix PP inconsistency with HiCache L3 (#22607)](https://github.com/sgl-project/sglang/pull/27010) — 36 comments · 3 reactions · open
- **Pull Request** [\[Model\] Support Ling-3.0-flash (BailingMoeV3)](https://github.com/sgl-project/sglang/pull/33561) — 10 comments · 9 reactions · open
- **Pull Request** [\[HiCache\] Dedup MLA KV cache in host memory across TP ranks](https://github.com/sgl-project/sglang/pull/26691) — 13 comments · 7 reactions · open
- **Pull Request** [\[PP&Spec\] enable speculative decoding (eagle_worker_v2) under PP](https://github.com/sgl-project/sglang/pull/31139) — 22 comments · 4 reactions · open
- **Pull Request** [\[AMD\] Fuse shared_expert_gate GEMV into the MoE append kernel (HIP/aiter)](https://github.com/sgl-project/sglang/pull/28666) — 26 comments · 1 reactions · closed
- **Pull Request** [\[AMD\]\[Quantization\] Online MXFP4 quantization 4/N - NVFP4 to MXFP4 Online Requantization on AMD GPUs](https://github.com/sgl-project/sglang/pull/29328) — 24 comments · 1 reactions · open
- **Pull Request** [\[HiCache\]: Optimize hybrid/DSA L3 prefetch result sync and usable-prefix clamping](https://github.com/sgl-project/sglang/pull/31443) — 22 comments · 1 reactions · closed
- **Issue** [\[AITER-Upgrade\] PR readiness](https://github.com/sgl-project/sglang/issues/21302) — 20 comments · 0 reactions · open
- **Pull Request** [\[MoE Refactor\] Migrate SM100 trtllm-gen mxfp4 MoE onto MoeRunner](https://github.com/sgl-project/sglang/pull/32405) — 20 comments · 1 reactions · open
- **Pull Request** [\[AMD\] Add fused all-reduce RMSNorm per-token FP8/MXFP4 quant](https://github.com/sgl-project/sglang/pull/29723) — 15 comments · 2 reactions · open
- **Pull Request** [\[NVIDIA\]\[comm\] Merge EP+MoE-TP post-experts all-reduces into one _TP reduction](https://github.com/sgl-project/sglang/pull/32963) — 22 comments · 0 reactions · open
- **Pull Request** [Graceful shutdown with SIGTERM for child processes](https://github.com/sgl-project/sglang/pull/16484) — 17 comments · 1 reactions · open
- **Pull Request** [perf(jit_kernel/deepseek_v4): optimize paged_mqa_metadata](https://github.com/sgl-project/sglang/pull/25855) — 20 comments · 0 reactions · closed
- **Pull Request** [\[AMD\] \[GLM5\] Skip DSA decode indexer when kv_len <= index_topk (dense k-only fast path)](https://github.com/sgl-project/sglang/pull/31324) — 15 comments · 1 reactions · open
- **Pull Request** [\[HiCache\] Fix sidecar pool life-time issue](https://github.com/sgl-project/sglang/pull/31668) — 7 comments · 4 reactions · open
- **Pull Request** [\[AMD\] Enable gfx1250 Support](https://github.com/sgl-project/sglang/pull/32754) — 15 comments · 1 reactions · open
- **Pull Request** [fix(ci): refresh nightly precision baseline from remote](https://github.com/sgl-project/sglang/pull/34668) — 18 comments · 0 reactions · open
- **Pull Request** [\[AMD\] GDN linear out-proj fusion](https://github.com/sgl-project/sglang/pull/28655) — 13 comments · 1 reactions · open
- **Pull Request** [\[XPU\]\[Diffusion\] Enable MiniMax H3 on XPU platforms](https://github.com/sgl-project/sglang/pull/33366) — 17 comments · 0 reactions · open
- **Pull Request** [TP/PP Consensus checker](https://github.com/sgl-project/sglang/pull/34406) — 1 comments · 4 reactions · open
- **Pull Request** [Profiling Enhancements \[2/3\]: detailed execution step annotations](https://github.com/sgl-project/sglang/pull/24911) — 10 comments · 1 reactions · open
- **Pull Request** [\[NPU\] Add mxfp4-w4a8 MOE Quantization Support for NPU](https://github.com/sgl-project/sglang/pull/30318) — 14 comments · 0 reactions · open
- **Pull Request** [\[GDN\] perf: Fuse the linear-attention prefill prologue for Flashinfer prefill attn](https://github.com/sgl-project/sglang/pull/30797) — 15 comments · 0 reactions · open
- **Pull Request** [\[AMD\] \[Docker\] Upgrade Python 3.12 + torch 2.11 + triton 3.7 in ROCm 7.2.4](https://github.com/sgl-project/sglang/pull/30984) — 15 comments · 0 reactions · open
- **Pull Request** [\[EPD\] Batch embedding cache host-device range copies](https://github.com/sgl-project/sglang/pull/31574) — 6 comments · 2 reactions · closed
- **Pull Request** [\[Spec\] Windowed draft-decode attention for built-in EAGLE / MTP drafts](https://github.com/sgl-project/sglang/pull/32673) — 11 comments · 1 reactions · open

### [Ray](https://github.com/ray-project/ray)

- **Issue** [\[serve\]\[llm\] s3:// model_source is dropped on Ray 2.57.0: engine config gets model_id instead of the staged local path](https://github.com/ray-project/ray/issues/65477) — 0 comments · 0 reactions · open
- **Issue** [\[Data\] Fused map functions are serialized with every shuffle-map task](https://github.com/ray-project/ray/issues/65479) — 0 comments · 0 reactions · open
- **Issue** [\[Data\] Extend StreamingRepartition non-strict fusion to Filter/MapRows/FlatMap](https://github.com/ray-project/ray/issues/63624) — 1 comments · 0 reactions · open
- **Pull Request** [\[serve\] Columnar zero-copy autoscaling-metrics ingest](https://github.com/ray-project/ray/pull/64281) — 2 comments · 1 reactions · open
- **Pull Request** [\[data\]\[llm\] Add vLLM engine metrics and request-latency overhead to single-node batch benchmark](https://github.com/ray-project/ray/pull/63912) — 14 comments · 1 reactions · open
- **Issue** [\[Ray serve\] Add Native Anthropic Messages API (/v1/messages) Support to Ray Serve LLM](https://github.com/ray-project/ray/issues/64965) — 3 comments · 1 reactions · open
- **Pull Request** [\[data\] Add orc datasource for V2](https://github.com/ray-project/ray/pull/64540) — 7 comments · 1 reactions · open
- **Pull Request** [\[docs\] vendor the KubeRay CRD API reference into the Ray docs](https://github.com/ray-project/ray/pull/65428) — 7 comments · 1 reactions · closed
- **Pull Request** [\[core\] Free local objects batching](https://github.com/ray-project/ray/pull/65000) — 1 comments · 2 reactions · open
- **Pull Request** [\[docs\] Add Kubernetes and KubeRay conventions to the style guide](https://github.com/ray-project/ray/pull/65239) — 4 comments · 1 reactions · closed
- **Pull Request** [\[jobs\]: return structured 503 when job logs are unavailable](https://github.com/ray-project/ray/pull/65405) — 4 comments · 1 reactions · open
- **Pull Request** [\[train\] Share PlacementGroupCleaner across Train runs](https://github.com/ray-project/ray/pull/65447) — 0 comments · 2 reactions · open
- **Pull Request** [\[Data\] Fix ResourceBudget backpressure causing pipeline stall](https://github.com/ray-project/ray/pull/64601) — 3 comments · 1 reactions · open
- **Pull Request** [\[Train\] Add NCCL RAS health callback](https://github.com/ray-project/ray/pull/64928) — 2 comments · 1 reactions · open
- **Pull Request** [\[core\] feat(rdt): enable driver-side ray.put with NIXL tensor transport](https://github.com/ray-project/ray/pull/65072) — 3 comments · 1 reactions · open
- **Pull Request** [\[TPU\] Add PyTorch TPU environment variable and runtime_env APIs to Slice and Subslice placement groups](https://github.com/ray-project/ray/pull/65221) — 3 comments · 1 reactions · open
- **Pull Request** [\[Data\]\[LLM\] Add multi-host TPU batch inference for Ray Data LLM](https://github.com/ray-project/ray/pull/65422) — 3 comments · 1 reactions · open
- **Pull Request** [\[docs\] Convert the nine highest-traffic landing pages from RST to MyST](https://github.com/ray-project/ray/pull/65467) — 2 comments · 1 reactions · closed
- **Pull Request** [\[doc\] Conversion tooling: render diff, card-grid mapping, and a soft-wrap skill](https://github.com/ray-project/ray/pull/65469) — 2 comments · 1 reactions · closed
- **Pull Request** [\[docs\] Convert the seven card-grid library front doors from RST to MyST](https://github.com/ray-project/ray/pull/65470) — 2 comments · 1 reactions · open
- **Issue** [\[Serve\] remove deprecated APIs, CLI flags, and schema fields](https://github.com/ray-project/ray/issues/62733) — 1 comments · 0 reactions · closed
- **Issue** [\[Data\] `test_tensor` flakes at the Bazel short-test timeout](https://github.com/ray-project/ray/issues/65481) — 0 comments · 0 reactions · closed
- **Pull Request** [Introducing Hostname Resolution for Nodes](https://github.com/ray-project/ray/pull/64350) — 1 comments · 2 reactions · open
- **Pull Request** [\[ci\] Add credential-free redirect-validation premerge check](https://github.com/ray-project/ray/pull/64413) — 1 comments · 1 reactions · closed
- **Pull Request** [\[Data\] Support appending a subset of columns to a Lance dataset.](https://github.com/ray-project/ray/pull/64474) — 4 comments · 1 reactions · open
- **Pull Request** [\[docs\] Add a scheduling overview with defaults to the Ray Core scheduling page](https://github.com/ray-project/ray/pull/65264) — 1 comments · 1 reactions · open
- **Pull Request** [\[Data\] \[5/11\] Add the Parquet FooterReader actor pool](https://github.com/ray-project/ray/pull/65273) — 1 comments · 1 reactions · open
- **Pull Request** [\[ci\] Count the Vale configuration and the API-consistency checker as documentation content in the docs-go scope guard](https://github.com/ray-project/ray/pull/65342) — 0 comments · 1 reactions · closed
- **Pull Request** [\[ci\] Remove the banned-words lint check in favor of Vale](https://github.com/ray-project/ray/pull/65368) — 0 comments · 1 reactions · closed
- **Pull Request** [\[ci\] Record why the Serve request-router API exemptions exist](https://github.com/ray-project/ray/pull/65369) — 0 comments · 1 reactions · closed

### [BentoML](https://github.com/bentoml/BentoML)

- **Pull Request** [feat: agent skills for deploying BentoML services to Kubernetes, EC2, and SageMaker](https://github.com/bentoml/BentoML/pull/5683) — 0 comments · 0 reactions · open
- **Pull Request** [fix: Windows tar symlink extraction and fastai CI dependency resolution](https://github.com/bentoml/BentoML/pull/5689) — 0 comments · 0 reactions · open
