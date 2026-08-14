# AI Infrastructure — 2026-08-14

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [\[Roadmap\] sglang auto tuner](https://github.com/sgl-project/sglang/issues/13363)

- Project: `sgl-project/sglang`
- Tier: `maintainer-invited`
- Evidence: Maintainers marked this as a good first issue; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [\[Feature\] Add KV cache usage prometheus metrics](https://github.com/sgl-project/sglang/issues/5979)

- Project: `sgl-project/sglang`
- Tier: `maintainer-invited`
- Evidence: Maintainers marked this as a good first issue; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [\[Bug\]: vllm/vllm-openai:latest fails to start Gemma4 with Transformers 5.15.0](https://github.com/vllm-project/vllm/issues/51744)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: Decode Context Parallelism (`--decode-context-parallel-size`) output drift and gibberish in v0.21.0 and latest nightly](https://github.com/vllm-project/vllm/issues/41623)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [LiteLLM](https://github.com/BerriAI/litellm)

- **Issue** [\[Feature\]: Dark Mode](https://github.com/BerriAI/litellm/issues/10177) — 63 comments · 84 reactions · open
- **Issue** [LiteLLM Proxy fails to start on Python 3.14 due to uvloop incompatibility](https://github.com/BerriAI/litellm/issues/20933) — 5 comments · 13 reactions · closed
- **Issue** [\[Feature\]: Support Anthropic-native response format for /v1/models endpoint (Claude Code gateway discovery)](https://github.com/BerriAI/litellm/issues/27180) — 5 comments · 8 reactions · closed
- **Pull Request** [feat: pre-adoption shadow eval for the auto-router (backend)](https://github.com/BerriAI/litellm/pull/36571) — 41 comments · 1 reactions · closed
- **Pull Request** [feat(ui): shadow eval section on the auto-router usage tab](https://github.com/BerriAI/litellm/pull/36572) — 50 comments · 1 reactions · closed
- **Pull Request** [feat(ui): shadow evals tab beside auto-router usage](https://github.com/BerriAI/litellm/pull/36588) — 46 comments · 1 reactions · closed
- **Pull Request** [fix(proxy): make /cursor/chat/completions work with Cursor agent mode](https://github.com/BerriAI/litellm/pull/34029) — 36 comments · 1 reactions · closed
- **Issue** [\[Bug\]: /metrics endpoint not allowing for unauthenticated access](https://github.com/BerriAI/litellm/issues/27926) — 3 comments · 7 reactions · open
- **Pull Request** [feat(cost): support time-based off-peak pricing in cost calculation](https://github.com/BerriAI/litellm/pull/31725) — 18 comments · 2 reactions · open
- **Pull Request** [fix(mcp): expose client HTTP headers to logging callbacks and hooks](https://github.com/BerriAI/litellm/pull/36724) — 23 comments · 1 reactions · closed
- **Issue** [\[Bug\]: Function tools fail with reasoning_effort error for OpenAI gpt-5.6 family models (gpt-5.6-sol/luna/terra) on /chat/completions](https://github.com/BerriAI/litellm/issues/33221) — 9 comments · 3 reactions · closed
- **Pull Request** [feat(proxy): proactive model deprecation alerts and `/model/deprecations` endpoint](https://github.com/BerriAI/litellm/pull/26900) — 18 comments · 1 reactions · open
- **Pull Request** [fix(openai): bridge gpt-5.6+ tools to /v1/responses without reasoning_effort](https://github.com/BerriAI/litellm/pull/34043) — 10 comments · 4 reactions · closed
- **Pull Request** [feat: pre-adoption shadow eval for the auto-router (blind pairwise judge, derived state)](https://github.com/BerriAI/litellm/pull/36587) — 19 comments · 1 reactions · closed
- **Pull Request** [perf(spend-logs): bound retention cleanup so one run cannot saturate the database](https://github.com/BerriAI/litellm/pull/36594) — 16 comments · 1 reactions · closed
- **Pull Request** [fix(ui): show indirectly granted and name-keyed MCP servers in the tool matrix](https://github.com/BerriAI/litellm/pull/35154) — 18 comments · 1 reactions · open
- **Pull Request** [feat(proxy): serve Anthropic-native /v1/models for Claude Code gateway discovery](https://github.com/BerriAI/litellm/pull/35455) — 6 comments · 3 reactions · open
- **Pull Request** [feat(realtime): support latest OpenAI audio models](https://github.com/BerriAI/litellm/pull/35600) — 10 comments · 2 reactions · open
- **Pull Request** [feat(complexity_router): calibrate the classifier rubric with worked examples, selectable per router](https://github.com/BerriAI/litellm/pull/36578) — 15 comments · 1 reactions · closed
- **Issue** [\[Bug\]: Xiaomi MiMo models: 'output_config' parameter causes AsyncCompletions.create() to fail with Claude Code](https://github.com/BerriAI/litellm/issues/24549) — 8 comments · 0 reactions · open
- **Issue** [\[Feature\]: Support time-based / peak-offpeak pricing for model cost calculation](https://github.com/BerriAI/litellm/issues/31606) — 1 comments · 2 reactions · open
- **Pull Request** [fix(s3_v2): URL-encode object keys to prevent SigV4 signature mismatch](https://github.com/BerriAI/litellm/pull/24585) — 8 comments · 3 reactions · open
- **Pull Request** [feat(azure-ai): add Grok 4.3 model metadata](https://github.com/BerriAI/litellm/pull/27932) — 8 comments · 2 reactions · closed
- **Pull Request** [fix(proxy/batches): stop forwarding custom_llm_provider twice in list and cancel](https://github.com/BerriAI/litellm/pull/32813) — 12 comments · 1 reactions · closed
- **Pull Request** [fix(ui): keep MCP tool allowlists for team servers granted indirectly](https://github.com/BerriAI/litellm/pull/35153) — 17 comments · 1 reactions · open
- **Pull Request** [feat(skills): self-service skill submission with admin review](https://github.com/BerriAI/litellm/pull/36677) — 12 comments · 1 reactions · open
- **Pull Request** [feat: shadow eval samples /v1/messages and /v1/responses traffic](https://github.com/BerriAI/litellm/pull/36830) — 17 comments · 1 reactions · open
- **Issue** [\[Bug\]: Vertex AI: Custom api_base credential skip logic missing in vertex_llm_base.py](https://github.com/BerriAI/litellm/issues/19138) — 11 comments · 0 reactions · open
- **Pull Request** [fix(anthropic): default thinking.display="summarized" on Claude Opus 4.7](https://github.com/BerriAI/litellm/pull/25967) — 14 comments · 1 reactions · closed
- **Pull Request** [feat(vertex): add Lyria model support](https://github.com/BerriAI/litellm/pull/30856) — 10 comments · 1 reactions · open

### [vLLM](https://github.com/vllm-project/vllm)

- **Pull Request** [\[MoE\]\[Offload\] Run MoE models exceeding VRAM via expert CPU offloading with GPU cache (--moe-expert-cache-size)](https://github.com/vllm-project/vllm/pull/37190) — 56 comments · 15 reactions · open
- **Pull Request** [Add Muse Glimmer model support](https://github.com/vllm-project/vllm/pull/51655) — 37 comments · 16 reactions · open
- **Issue** [\[Performance\]: Deepseek-V4 Support and Optimization on ROCm Backend](https://github.com/vllm-project/vllm/issues/41820) — 15 comments · 7 reactions · open
- **Pull Request** [\[Core\] Extensible (growable) KV cache](https://github.com/vllm-project/vllm/pull/50779) — 20 comments · 5 reactions · open
- **Pull Request** [refactor(envs): migrate vllm/envs.py to pydantic-settings](https://github.com/vllm-project/vllm/pull/42136) — 28 comments · 3 reactions · open
- **Pull Request** [\[Core\]\[V1\] Support trace_decode_token_ids for deterministic decode replay](https://github.com/vllm-project/vllm/pull/46701) — 20 comments · 3 reactions · open
- **Pull Request** [\[Model\] Apertus 1.5](https://github.com/vllm-project/vllm/pull/50496) — 15 comments · 8 reactions · open
- **Pull Request** [\[Kimi-K3\] Add GEMM-RS for sequence parallelism](https://github.com/vllm-project/vllm/pull/52079) — 8 comments · 3 reactions · closed
- **Pull Request** [\[Perf\] Integrate flash-maxsim Triton kernels for late-interaction scoring](https://github.com/vllm-project/vllm/pull/40337) — 30 comments · 3 reactions · open
- **Pull Request** [\[Bugfix\] Correct prompt lengths for timed_traces benchmark](https://github.com/vllm-project/vllm/pull/45423) — 5 comments · 3 reactions · closed
- **Pull Request** [\[Model\]\[Spec Decode\] Tap the pre-norm AttnRes mixture as the Kimi K3 DFlash aux state](https://github.com/vllm-project/vllm/pull/50487) — 28 comments · 3 reactions · open
- **Pull Request** [\[MoE\] Generalize masked activation for padded layouts](https://github.com/vllm-project/vllm/pull/51217) — 13 comments · 2 reactions · open
- **Pull Request** [\[Core\]\[WIP\] Check for GPU<->CPU sync during CI](https://github.com/vllm-project/vllm/pull/43107) — 25 comments · 3 reactions · open
- **Pull Request** [\[5/N\]\[KV-Cache Layout Refactor\] Backend-published KV packing via customize_spec](https://github.com/vllm-project/vllm/pull/51704) — 28 comments · 2 reactions · open
- **Pull Request** [\[ROCm\] Defer `tilelang` import through its import `from vllm.tilelang_utils import tilelang` and relaxed `has_tilelang`](https://github.com/vllm-project/vllm/pull/51159) — 26 comments · 2 reactions · closed
- **Pull Request** [\[K3\] support recoverssm for K3](https://github.com/vllm-project/vllm/pull/51855) — 3 comments · 2 reactions · open
- **Pull Request** [Add `pydocstyle` to the `ruff` rules](https://github.com/vllm-project/vllm/pull/52136) — 3 comments · 2 reactions · open
- **Pull Request** [\[Kernel\] ReplaySSM: cache SSM inputs for faster Gated DeltaNet standard decode](https://github.com/vllm-project/vllm/pull/48792) — 5 comments · 2 reactions · open
- **Pull Request** [Add SM90 FA4 Dense and MLA](https://github.com/vllm-project/vllm/pull/51416) — 5 comments · 2 reactions · open
- **Pull Request** [\[6/N\]\[KV-Cache Layout Refactor\] Standardize KV cache layout](https://github.com/vllm-project/vllm/pull/51718) — 6 comments · 0 reactions · open
- **Pull Request** [\[ROCm\]\[CI\] Gating more ROCm tests](https://github.com/vllm-project/vllm/pull/44969) — 20 comments · 2 reactions · open
- **Pull Request** [\[KV-offload\]\[FS\]: Batching for read/write threads](https://github.com/vllm-project/vllm/pull/49225) — 20 comments · 2 reactions · open
- **Pull Request** [\[ModelOpt\] Redesign the LinearMethod classes using the generic QuantKey-driven method](https://github.com/vllm-project/vllm/pull/49381) — 21 comments · 2 reactions · open
- **Pull Request** [\[ROCm\]Remove special-case SiTU support model-specific gating](https://github.com/vllm-project/vllm/pull/50597) — 21 comments · 2 reactions · open
- **Pull Request** [buffer size insuffient Dspark sd for FlashInfer MNNVL allreduce](https://github.com/vllm-project/vllm/pull/50932) — 21 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\] Make DSV4 sparse MLA work end-to-end for plain decode, MTP, and DSpark](https://github.com/vllm-project/vllm/pull/51538) — 20 comments · 2 reactions · open
- **Pull Request** [fix(v1): decouple async Mamba align D2H counts from InputBatch row shifts (#51571)](https://github.com/vllm-project/vllm/pull/51599) — 20 comments · 2 reactions · open
- **Pull Request** [\[Feature\]\[KVConnector\] Add optional get_eviction_order hook for policy-driven free-queue ordering](https://github.com/vllm-project/vllm/pull/42799) — 3 comments · 1 reactions · open
- **Issue** [\[ROCm\]\[AMD\] Kimi-K3 Gap and Roadmap Tracking](https://github.com/vllm-project/vllm/issues/50682) — 16 comments · 0 reactions · open
- **Pull Request** [\[EPD\] Add ECMooncakeConnector for encoder cache over Mooncake TransferEngine](https://github.com/vllm-project/vllm/pull/41567) — 4 comments · 5 reactions · open

### [SGLang](https://github.com/sgl-project/sglang)

- **Issue** [\[Feature\] Kimi K3 Roadmap](https://github.com/sgl-project/sglang/issues/32607) — 8 comments · 22 reactions · open
- **Pull Request** [\[Feature\] Support Efficient Sparse HiP Attention (InfiniteHiP) with Long-Context Generalization and KV Offloading Capabilties](https://github.com/sgl-project/sglang/pull/3930) — 34 comments · 8 reactions · closed
- **Issue** [\[Tracking\] CI Test Failures and Fixes](https://github.com/sgl-project/sglang/issues/17050) — 13 comments · 10 reactions · open
- **Pull Request** [\[P/D disagg\] Decode-side radix cache for SWA hybrid models (unified radix tree)](https://github.com/sgl-project/sglang/pull/27770) — 38 comments · 3 reactions · open
- **Issue** [\[Feature\] Improve Unit Test Coverage](https://github.com/sgl-project/sglang/issues/20865) — 83 comments · 0 reactions · open
- **Pull Request** [\[HiCache\] Fix PP inconsistency with HiCache L3 (#22607)](https://github.com/sgl-project/sglang/pull/27010) — 36 comments · 3 reactions · open
- **Pull Request** [\[FlashInfer v0.6.16\] Support FlashInfer CuTe DSL NVFP4 MoE quantization](https://github.com/sgl-project/sglang/pull/28354) — 42 comments · 0 reactions · closed
- **Pull Request** [\[DSv4\] Integrate TRT-LLM DSv4 Attention for SM100/103](https://github.com/sgl-project/sglang/pull/30805) — 43 comments · 0 reactions · open
- **Issue** [\[NVIDIA\] DeepSeek V4 Perf Tracking](https://github.com/sgl-project/sglang/issues/33636) — 8 comments · 5 reactions · open
- **Issue** [\[Roadmap\] Integrate NCCL 2.30 Features into SGLang](https://github.com/sgl-project/sglang/issues/32774) — 1 comments · 7 reactions · open
- **Pull Request** [\[AMD\] Fuse shared_expert_gate GEMV into the MoE append kernel (HIP/aiter)](https://github.com/sgl-project/sglang/pull/28666) — 26 comments · 1 reactions · open
- **Pull Request** [\[AMD\]\[Quantization\] Online MXFP4 quantization 4/N - NVFP4 to MXFP4 Online Requantization on AMD GPUs](https://github.com/sgl-project/sglang/pull/29328) — 22 comments · 1 reactions · open
- **Pull Request** [\[AMD\] sgl-kernel: enable gfx1151 (RDNA3.5 / Strix Halo) for single-GPU](https://github.com/sgl-project/sglang/pull/31137) — 9 comments · 5 reactions · open
- **Pull Request** [support qwen 3.8](https://github.com/sgl-project/sglang/pull/34585) — 0 comments · 6 reactions · open
- **Pull Request** [\[MoE Refactor\] Migrate SM100 trtllm-gen mxfp4 MoE onto MoeRunner](https://github.com/sgl-project/sglang/pull/32405) — 19 comments · 1 reactions · open
- **Pull Request** [feat: add "balance" option and implement for "--ep-dispatch-algorithm"](https://github.com/sgl-project/sglang/pull/6739) — 13 comments · 3 reactions · closed
- **Pull Request** [\[AMD\] \[GLM5\] Enable dense-MHA short-context prefill fallback on gfx950](https://github.com/sgl-project/sglang/pull/30808) — 19 comments · 0 reactions · open
- **Pull Request** [Graceful shutdown with SIGTERM for child processes](https://github.com/sgl-project/sglang/pull/16484) — 17 comments · 1 reactions · open
- **Pull Request** [\[AMD\] \[GLM5\] Skip DSA decode indexer when kv_len <= index_topk (dense k-only fast path)](https://github.com/sgl-project/sglang/pull/31324) — 13 comments · 1 reactions · open
- **Pull Request** [\[AMD\] Enable gfx1250 Support](https://github.com/sgl-project/sglang/pull/32754) — 13 comments · 1 reactions · open
- **Pull Request** [Profiling Enhancements \[2/3\]: detailed execution step annotations](https://github.com/sgl-project/sglang/pull/24911) — 10 comments · 1 reactions · open
- **Pull Request** [\[NPU\] Add Ascend NPU support for DeepSeek-V4](https://github.com/sgl-project/sglang/pull/25144) — 18 comments · 0 reactions · closed
- **Pull Request** [perf(jit_kernel/deepseek_v4): optimize paged_mqa_metadata](https://github.com/sgl-project/sglang/pull/25855) — 19 comments · 0 reactions · closed
- **Pull Request** [\[GDN\] perf: Fuse the linear-attention prefill prologue for Flashinfer prefill attn](https://github.com/sgl-project/sglang/pull/30797) — 14 comments · 0 reactions · open
- **Pull Request** [\[AMD\] \[Docker\] Upgrade Python 3.12 + torch 2.11 + triton 3.7 in ROCm 7.2.4](https://github.com/sgl-project/sglang/pull/30984) — 15 comments · 0 reactions · open
- **Pull Request** [\[Spec\] Windowed draft-decode attention for built-in EAGLE / MTP drafts](https://github.com/sgl-project/sglang/pull/32673) — 11 comments · 1 reactions · open
- **Pull Request** [\[XPU\]\[Diffusion\] Enable MiniMax H3 on XPU platforms](https://github.com/sgl-project/sglang/pull/33366) — 15 comments · 0 reactions · open
- **Pull Request** [fix(ci): refresh nightly precision baseline from remote](https://github.com/sgl-project/sglang/pull/34668) — 14 comments · 0 reactions · open
- **Pull Request** [XPU: Enable GLM5.1 (GlmMoeDsaForCausalLM) DSA Attention](https://github.com/sgl-project/sglang/pull/24959) — 8 comments · 1 reactions · open
- **Pull Request** [\[NPU\] Add mxfp4-w4a8 MOE Quantization Support for NPU](https://github.com/sgl-project/sglang/pull/30318) — 12 comments · 0 reactions · open

### [Ray](https://github.com/ray-project/ray)

- **Issue** [RDT: ray.put(list, _tensor_transport=...): batch-put a list of objects and get back a list of refs](https://github.com/ray-project/ray/issues/64715) — 3 comments · 0 reactions · closed
- **Issue** [RDT: Support different destination memory from source memory](https://github.com/ray-project/ray/issues/64711) — 1 comments · 0 reactions · closed
- **Issue** [\[data\] Fanout into independently schedulable one-row blocks has very high overhead](https://github.com/ray-project/ray/issues/65473) — 0 comments · 0 reactions · open
- **Issue** [\[core\]\[rdt\] Reduce O(N) overheads in RDT NIXL backend](https://github.com/ray-project/ray/issues/65475) — 0 comments · 0 reactions · open
- **Issue** [\[serve\]\[llm\] s3:// model_source is dropped on Ray 2.57.0: engine config gets model_id instead of the staged local path](https://github.com/ray-project/ray/issues/65477) — 0 comments · 0 reactions · open
- **Pull Request** [\[Core\] Mobilint Accelerator Support](https://github.com/ray-project/ray/pull/61898) — 7 comments · 3 reactions · closed
- **Pull Request** [\[docs\] vendor the KubeRay CRD API reference into the Ray docs](https://github.com/ray-project/ray/pull/65428) — 7 comments · 1 reactions · open
- **Pull Request** [\[Data\]\[1/N\] add external shuffle runtime library](https://github.com/ray-project/ray/pull/64828) — 4 comments · 1 reactions · open
- **Pull Request** [\[docs\] Add Kubernetes and KubeRay conventions to the style guide](https://github.com/ray-project/ray/pull/65239) — 4 comments · 1 reactions · open
- **Pull Request** [fix(jobs): return structured 503 when job logs are unavailable](https://github.com/ray-project/ray/pull/65405) — 4 comments · 1 reactions · open
- **Pull Request** [\[train\] Share PlacementGroupCleaner across Train runs](https://github.com/ray-project/ray/pull/65447) — 0 comments · 2 reactions · open
- **Pull Request** [\[Serve\]\[LLM\] Pass remote URI as model for streaming load formats](https://github.com/ray-project/ray/pull/64996) — 3 comments · 2 reactions · open
- **Pull Request** [\[core\] feat(rdt): enable driver-side ray.put with NIXL tensor transport](https://github.com/ray-project/ray/pull/65072) — 2 comments · 1 reactions · open
- **Pull Request** [\[Data\] Throttle OutputBackpressureGuard releases with a per-op interval](https://github.com/ray-project/ray/pull/65202) — 3 comments · 1 reactions · open
- **Issue** [\[core\]\[rdt\] Receiver side pre-registered memory pool](https://github.com/ray-project/ray/issues/60443) — 1 comments · 0 reactions · closed
- **Issue** [\[Data\] Replace ray_remote_args with named options on Dataset transformations](https://github.com/ray-project/ray/issues/65227) — 0 comments · 0 reactions · closed
- **Issue** [\[Data\] Fused map functions are serialized with every shuffle-map task](https://github.com/ray-project/ray/issues/65479) — 0 comments · 0 reactions · open
- **Pull Request** [\[Data\] Add DataIterator.count() to get dataset/shard size](https://github.com/ray-project/ray/pull/64869) — 4 comments · 1 reactions · open
- **Pull Request** [\[core\] Free local objects batching](https://github.com/ray-project/ray/pull/65000) — 1 comments · 2 reactions · open
- **Pull Request** [\[Data\] Deprecate `ray_remote_args` for Dataset transformations](https://github.com/ray-project/ray/pull/65228) — 1 comments · 1 reactions · closed
- **Pull Request** [\[CI\] Make the Vale pre-commit hook run, and upgrade Vale to 3.17.1](https://github.com/ray-project/ray/pull/65375) — 0 comments · 1 reactions · open
- **Pull Request** [\[Data\] OpTask._cancel never passes force=True](https://github.com/ray-project/ray/pull/65389) — 0 comments · 1 reactions · open
- **Pull Request** [\[core\]\[rdt\] nixl: allow pool to serve tensors on a different device](https://github.com/ray-project/ray/pull/65418) — 0 comments · 1 reactions · open
- **Pull Request** [\[serve\] Deflake test_cli by adding explicit wait timeouts and stopping tracing config leak](https://github.com/ray-project/ray/pull/65432) — 0 comments · 1 reactions · closed
- **Pull Request** [refactor(setup): modernize string formatting and ensure explicit file encoding](https://github.com/ray-project/ray/pull/65439) — 1 comments · 1 reactions · open
- **Pull Request** [\[TPU\] Rename dispatch to run_on_slice](https://github.com/ray-project/ray/pull/65442) — 0 comments · 1 reactions · open
- **Pull Request** [\[doc\] Render the Jobs API spec with sphinxcontrib-openapi instead of ReDoc](https://github.com/ray-project/ray/pull/65460) — 0 comments · 1 reactions · open
- **Pull Request** [\[doc\] llms.txt: tell agents the page links also serve Markdown](https://github.com/ray-project/ray/pull/65461) — 0 comments · 1 reactions · open
- **Pull Request** [\[docs\] Sync the vendored KubeRay CRD API reference](https://github.com/ray-project/ray/pull/65462) — 1 comments · 1 reactions · closed
- **Pull Request** [core: release runtime env per-job loggers](https://github.com/ray-project/ray/pull/65463) — 0 comments · 1 reactions · open

### [BentoML](https://github.com/bentoml/BentoML)

No new or materially changed signals.
