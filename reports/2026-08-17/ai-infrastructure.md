# AI Infrastructure — 2026-08-17

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [\[Feature\]: Tracking Whisper feature requests](https://github.com/vllm-project/vllm/issues/25750)

- Project: `vllm-project/vllm`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: help wanted, good first issue; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [\[Roadmap\] sglang auto tuner](https://github.com/sgl-project/sglang/issues/13363)

- Project: `sgl-project/sglang`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: good first issue; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [\[Bug\]: Kimi-K2.6 intermittently outputs only "!!!!!!!!!!" in reasoning field with content null](https://github.com/vllm-project/vllm/issues/42426)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: chatgpt/gpt-5.4 returns empty final Responses output, and completion() bridge fails with "Unknown items in responses API response: \[\]"](https://github.com/BerriAI/litellm/issues/25429)

- Project: `BerriAI/litellm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: Qwen3.5 CUDA Illegal Memory Access in GDN Kernel](https://github.com/vllm-project/vllm/issues/34948)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Data\] Modify maximum memory to OOM prevention guidance](https://github.com/ray-project/ray/issues/65508)

- Project: `ray-project/ray`
- Tier: `triage-lead`
- Evidence: Documentation-related issue with no assignee listed
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: upgrade vllm from 0.26.0 to 0.27.0 run deepseek v4 flash error](https://github.com/vllm-project/vllm/issues/51758)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: Batch invariance breaks with torch.compile and/or CUDA graphs on SM<90](https://github.com/vllm-project/vllm/issues/39096)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: AttributeError: 'ParallelLMHead' object has no attribute 'output_size_per_partition'](https://github.com/vllm-project/vllm/issues/52434)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: AssertionError: n_physical_experts=256 must be divisible by ep_size=3. Adjust num_redundant_experts.](https://github.com/vllm-project/vllm/issues/52435)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [LiteLLM](https://github.com/BerriAI/litellm)

- **Issue** [\[Feature\]: Support Langfuse Python SDK v4](https://github.com/BerriAI/litellm/issues/24123) — 9 comments · 15 reactions · open
- **Issue** [\[Bug\]: AnthropicException 400 - vector_store_ids: Extra inputs are not permitted](https://github.com/BerriAI/litellm/issues/23741) — 13 comments · 12 reactions · open
- **Pull Request** [feat(ui): add comprehensive dark mode support to dashboard](https://github.com/BerriAI/litellm/pull/18293) — 16 comments · 13 reactions · closed
- **Release** [v1.97.0](https://github.com/BerriAI/litellm/releases/tag/v1.97.0) — 
- **Release** [v1.98.0-rc.1](https://github.com/BerriAI/litellm/releases/tag/v1.98.0-rc.1) — 
- **Issue** [\[Bug\]: Pods get OOM Killed due to continous increase in memory.](https://github.com/BerriAI/litellm/issues/25219) — 14 comments · 6 reactions · open
- **Issue** [\[Bug\]: chatgpt/gpt-5.4 returns empty final Responses output, and completion() bridge fails with "Unknown items in responses API response: \[\]"](https://github.com/BerriAI/litellm/issues/25429) — 19 comments · 4 reactions · open
- **Issue** [\[Bug\]: Wildcard entries appear as models in the /models endpoint](https://github.com/BerriAI/litellm/issues/13752) — 6 comments · 7 reactions · closed
- **Issue** [Helm Chart: Switch to other repo provider for postgres and redis dependencies](https://github.com/BerriAI/litellm/issues/19769) — 8 comments · 5 reactions · open
- **Issue** [\[Feature\]: Support Azure AI Foundry Agents v2 (Responses API with agent_reference)](https://github.com/BerriAI/litellm/issues/25372) — 5 comments · 4 reactions · open
- **Pull Request** [fix(streaming): backfill response.completed output from output_item.done events](https://github.com/BerriAI/litellm/pull/31332) — 17 comments · 3 reactions · open
- **Pull Request** [feat(proxy): add project-level ITPM and OTPM quotas](https://github.com/BerriAI/litellm/pull/35110) — 21 comments · 1 reactions · open
- **Issue** [adaptive_router: one persisted alpha/beta=0 cell bricks the whole router with 500 gammavariate: alpha and beta must be > 0.0](https://github.com/BerriAI/litellm/issues/35590) — 2 comments · 2 reactions · open
- **Pull Request** [fix(pricing): add the azure gpt-realtime-2 family and price realtime image input per token](https://github.com/BerriAI/litellm/pull/31565) — 12 comments · 1 reactions · open
- **Pull Request** [fix(batches): support AWS Bedrock batch cancellation via `StopModelInvocationJob`](https://github.com/BerriAI/litellm/pull/34087) — 13 comments · 1 reactions · open
- **Pull Request** [feat(ui): add dashboard dark mode (rebase of #18293)](https://github.com/BerriAI/litellm/pull/35615) — 8 comments · 2 reactions · open
- **Pull Request** [fix(proxy): register WebSocket passthrough for OpenAI prefixes](https://github.com/BerriAI/litellm/pull/36151) — 16 comments · 1 reactions · open
- **Pull Request** [fix(bedrock): register managed-batch litellm_params so they stop leaking to the provider](https://github.com/BerriAI/litellm/pull/36633) — 13 comments · 1 reactions · closed
- **Issue** [\[Bug\]: config.yaml does not appear to exist in the OpenAPI spec anymore](https://github.com/BerriAI/litellm/issues/16623) — 6 comments · 1 reactions · open
- **Issue** [\[Bug\]: `timeout` silently ignored for Bedrock and Vertex AI streaming requests](https://github.com/BerriAI/litellm/issues/23375) — 2 comments · 2 reactions · closed
- **Pull Request** [feat(chatgpt): support image generation](https://github.com/BerriAI/litellm/pull/27931) — 14 comments · 1 reactions · open
- **Pull Request** [fix(proxy): accept virtual keys on include_subpath pass-through sub-paths](https://github.com/BerriAI/litellm/pull/36389) — 10 comments · 1 reactions · open
- **Pull Request** [fix(batches): account a managed batch's cost exactly once](https://github.com/BerriAI/litellm/pull/36877) — 11 comments · 1 reactions · closed
- **Pull Request** [feat: same-provider canonical model-name resolution (unknown-spelling requests route to the deployment that provably serves them)](https://github.com/BerriAI/litellm/pull/37035) — 10 comments · 1 reactions · open
- **Issue** [\[Feature\]: Support Exponential Backoff for completion()](https://github.com/BerriAI/litellm/issues/16068) — 8 comments · 0 reactions · closed
- **Pull Request** [feat: add stable gemini-3.1-flash-lite and deprecate preview in model_prices_and_context_window.json](https://github.com/BerriAI/litellm/pull/27627) — 4 comments · 3 reactions · open
- **Pull Request** [fix(batches): don't crash logging when a completed batch has no output file](https://github.com/BerriAI/litellm/pull/34067) — 9 comments · 1 reactions · open
- **Pull Request** [feat(openinfer): add OpenInfer as an OpenAI-compatible provider](https://github.com/BerriAI/litellm/pull/34623) — 9 comments · 1 reactions · open
- **Pull Request** [fix(bedrock): report uploaded size in the FileObject returned by managed batch uploads](https://github.com/BerriAI/litellm/pull/36392) — 8 comments · 1 reactions · open
- **Pull Request** [fix(bedrock): resolve the managed-batch output bucket on every path that reads it](https://github.com/BerriAI/litellm/pull/36634) — 9 comments · 1 reactions · closed

### [vLLM](https://github.com/vllm-project/vllm)

- **Issue** [\[Feature\]: Batch Invariant Feature and Performance Optimization](https://github.com/vllm-project/vllm/issues/27433) — 70 comments · 32 reactions · open
- **Issue** [\[Feature\]: Tracking Whisper feature requests](https://github.com/vllm-project/vllm/issues/25750) — 21 comments · 17 reactions · open
- **Issue** [\[Bug\]: Kimi-K2.6 intermittently outputs only "!!!!!!!!!!" in reasoning field with content null](https://github.com/vllm-project/vllm/issues/42426) — 93 comments · 6 reactions · open
- **Pull Request** [\[Core\] Extensible (growable) KV cache](https://github.com/vllm-project/vllm/pull/50779) — 24 comments · 5 reactions · open
- **Pull Request** [\[Core\]\[V1\] Support trace_decode_token_ids for deterministic decode replay](https://github.com/vllm-project/vllm/pull/46701) — 22 comments · 3 reactions · open
- **Issue** [\[Feature\]: Composite model loading using `AutoWeightsLoader` for all models](https://github.com/vllm-project/vllm/issues/15697) — 46 comments · 0 reactions · open
- **Pull Request** [\[ROCm\]\[DSV4\]\[Perf\] Optimize Triton sparse-MLA decode on gfx950](https://github.com/vllm-project/vllm/pull/52212) — 7 comments · 2 reactions · closed
- **Pull Request** [\[Bugfix\]\[Spec Decode\]\[Structured Output\] DSpark: fix the grammar bitmask mapping when the draft budget is zero](https://github.com/vllm-project/vllm/pull/52436) — 30 comments · 2 reactions · closed
- **Issue** [\[Bug\]: Qwen3.5 CUDA Illegal Memory Access in GDN Kernel](https://github.com/vllm-project/vllm/issues/34948) — 24 comments · 2 reactions · open
- **Pull Request** [Enable return_routed_experts support with CPU KV offload](https://github.com/vllm-project/vllm/pull/45635) — 25 comments · 3 reactions · open
- **Pull Request** [\[6/N\]\[KV-Cache Layout Refactor\] Standardize KV cache layout](https://github.com/vllm-project/vllm/pull/51718) — 12 comments · 0 reactions · open
- **Pull Request** [\[K3\] support recoverssm for K3](https://github.com/vllm-project/vllm/pull/51855) — 4 comments · 2 reactions · open
- **Pull Request** [\[Kernel\]\[Model\] Add manual CUDA RoPE KV-cache fusion for Llama](https://github.com/vllm-project/vllm/pull/52363) — 4 comments · 2 reactions · open
- **Pull Request** [\[ModelRunner V2\] Speculative Decoding NGram GPU Implementations](https://github.com/vllm-project/vllm/pull/40704) — 23 comments · 3 reactions · open
- **Pull Request** [\[ModelRunner v2\] Enable MRV2 for pooling models by default](https://github.com/vllm-project/vllm/pull/48290) — 23 comments · 3 reactions · open
- **Pull Request** [\[Bugfix\] Handle DeepseekV4ForCausalLM in benchmark_moe get_model_params](https://github.com/vllm-project/vllm/pull/52044) — 3 comments · 2 reactions · open
- **Issue** [\[Bug\]: upgrade vllm from 0.26.0 to 0.27.0 run deepseek v4 flash error](https://github.com/vllm-project/vllm/issues/51758) — 20 comments · 1 reactions · open
- **Pull Request** [\[kv_offload\] Session Aware Eviction Policy](https://github.com/vllm-project/vllm/pull/50422) — 5 comments · 2 reactions · open
- **Pull Request** [\[Attention\]\[MLA\] Add GLM-5.2 TurboQuant sparse backend with DCP/MTP](https://github.com/vllm-project/vllm/pull/52472) — 1 comments · 2 reactions · open
- **Issue** [\[Performance\]: vllm 19.0 online server测试波动偏大](https://github.com/vllm-project/vllm/issues/40001) — 2 comments · 0 reactions · closed
- **Issue** [\[Feature\]: Make DS layout used by default](https://github.com/vllm-project/vllm/issues/42882) — 2 comments · 0 reactions · open
- **Pull Request** [\[ModelOpt\] Redesign the LinearMethod classes using the generic QuantKey-driven method](https://github.com/vllm-project/vllm/pull/49381) — 23 comments · 2 reactions · open
- **Pull Request** [\[Kimi-K3\]\[AMD\] Return KDA and MLA projection outputs directly](https://github.com/vllm-project/vllm/pull/50592) — 22 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\]\[Kernel\] Fix divergent warp collectives in partial NeoX QK-Norm+RoPE](https://github.com/vllm-project/vllm/pull/50903) — 23 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\] Keep top-level quantization_config when benchmark_moe descends via --model-prefix](https://github.com/vllm-project/vllm/pull/51353) — 2 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\] Temporarily disable FA4 head-dim 256](https://github.com/vllm-project/vllm/pull/52050) — 23 comments · 2 reactions · closed
- **Pull Request** [\[Feat\]\[Bench\] Allow random dataset to sample real tokens from --dataset-path](https://github.com/vllm-project/vllm/pull/52537) — 3 comments · 2 reactions · open
- **Pull Request** [\[Performance\] Vectorize EPLB packing across MoE layers](https://github.com/vllm-project/vllm/pull/52556) — 1 comments · 2 reactions · open
- **Issue** [\[Installation\]: 有提供cuda 12.6+python3.12的vllm预编译的whl包吗？ 以开发者模型需要本地安装下，发布的都是cuda13版本的，不适配cuda12.6的本机的版本型号](https://github.com/vllm-project/vllm/issues/40343) — 2 comments · 4 reactions · open
- **Pull Request** [RISC-V ILP Optimization: Add instruction-level parallelism for transcendental functions](https://github.com/vllm-project/vllm/pull/42900) — 2 comments · 1 reactions · open

### [SGLang](https://github.com/sgl-project/sglang)

- **Issue** [\[Roadmap\] sglang auto tuner](https://github.com/sgl-project/sglang/issues/13363) — 15 comments · 29 reactions · open
- **Issue** [\[Tracking\] CI Test Failures and Fixes](https://github.com/sgl-project/sglang/issues/17050) — 13 comments · 10 reactions · open
- **Issue** [\[Feature\] Improve Unit Test Coverage](https://github.com/sgl-project/sglang/issues/20865) — 87 comments · 0 reactions · open
- **Pull Request** [\[HiCache\] Fix PP inconsistency with HiCache L3 (#22607)](https://github.com/sgl-project/sglang/pull/27010) — 36 comments · 3 reactions · open
- **Pull Request** [\[Model\] Support Ling-3.0-flash (BailingMoeV3)](https://github.com/sgl-project/sglang/pull/33561) — 10 comments · 9 reactions · open
- **Pull Request** [\[HiCache\] Dedup MLA KV cache in host memory across TP ranks](https://github.com/sgl-project/sglang/pull/26691) — 13 comments · 7 reactions · open
- **Pull Request** [\[DSv4\] Integrate TRT-LLM DSv4 Attention for SM100/103](https://github.com/sgl-project/sglang/pull/30805) — 46 comments · 0 reactions · open
- **Issue** [AMD Development Roadmap (2026 Q2)](https://github.com/sgl-project/sglang/issues/23494) — 10 comments · 4 reactions · open
- **Pull Request** [\[SM120&90\] Add CUDA fused Triton sparse-MLA prefill backend for DSA](https://github.com/sgl-project/sglang/pull/32779) — 10 comments · 0 reactions · open
- **Pull Request** [\[AMD\] Add fused all-reduce RMSNorm per-token FP8/MXFP4 quant](https://github.com/sgl-project/sglang/pull/29723) — 15 comments · 2 reactions · open
- **Pull Request** [\[AMD\] \[GLM5\] Skip DSA decode indexer when kv_len <= index_topk (dense k-only fast path)](https://github.com/sgl-project/sglang/pull/31324) — 16 comments · 1 reactions · closed
- **Pull Request** [\[AMD\] Enable gfx1250 Support](https://github.com/sgl-project/sglang/pull/32754) — 17 comments · 1 reactions · open
- **Pull Request** [vlm: streamline vision sdpa reshapes](https://github.com/sgl-project/sglang/pull/34991) — 0 comments · 0 reactions · closed
- **Pull Request** [\[Diffusion\] Reuse SRT SigLIP in Pi0.5](https://github.com/sgl-project/sglang/pull/34992) — 0 comments · 0 reactions · open
- **Pull Request** [\[NPU\] Add mxfp4-w4a8 MOE Quantization Support for NPU](https://github.com/sgl-project/sglang/pull/30318) — 18 comments · 0 reactions · closed
- **Pull Request** [\[NPU\] \[Diffusion\] Support MiniMax H3 on Ascend NPU's](https://github.com/sgl-project/sglang/pull/33569) — 18 comments · 0 reactions · open
- **Pull Request** [\[Feature\] Add suffix decoding speculative algorithm](https://github.com/sgl-project/sglang/pull/13553) — 17 comments · 1 reactions · closed
- **Pull Request** [\[AMD\] \[GLM5\] fp8 MLA absorbed bmm for GLM-5.2 on gfx950](https://github.com/sgl-project/sglang/pull/30519) — 9 comments · 2 reactions · open
- **Pull Request** [\[DSA\] Skip indexer KV cache for skip-topk layers](https://github.com/sgl-project/sglang/pull/30531) — 16 comments · 0 reactions · open
- **Pull Request** [\[AMD\]\[Fix\] Qwen3.5: guard zero-grid launch in fused_qk_gemma_rmsnorm(_with_gate) (HIP invalid configuration on idle DP rank)](https://github.com/sgl-project/sglang/pull/31794) — 9 comments · 2 reactions · closed
- **Pull Request** [TP/PP Consensus checker](https://github.com/sgl-project/sglang/pull/34406) — 1 comments · 4 reactions · open
- **Pull Request** [Profiling Enhancements \[2/3\]: detailed execution step annotations](https://github.com/sgl-project/sglang/pull/24911) — 10 comments · 1 reactions · open
- **Pull Request** [\[Spec\] Fix Dspark and Dflash state divergence across TP rank](https://github.com/sgl-project/sglang/pull/33614) — 15 comments · 0 reactions · open
- **Pull Request** [fix(bcg): preserve Qwen3-VL DeepStack inputs during replay](https://github.com/sgl-project/sglang/pull/33726) — 14 comments · 0 reactions · open
- **Pull Request** [XPU: Enable GLM5.1 (GlmMoeDsaForCausalLM) DSA Attention](https://github.com/sgl-project/sglang/pull/24959) — 8 comments · 1 reactions · open
- **Pull Request** [\[Simulator\] Add high-fidelity CPU-based inference simulator](https://github.com/sgl-project/sglang/pull/33824) — 12 comments · 0 reactions · open
- **Pull Request** [\[HiCache\] Buffer-only mode for HiCache host memory layer](https://github.com/sgl-project/sglang/pull/34798) — 1 comments · 3 reactions · open
- **Issue** [\[Feature\] W4A8 MoE kernel for NVFP4 models on non-Blackwell GPUs (SM90)](https://github.com/sgl-project/sglang/issues/22459) — 7 comments · 0 reactions · closed
- **Issue** [\[DFlash\] Infinite loop when using repetition_penalty — missing token accumulation and scaling penalties](https://github.com/sgl-project/sglang/issues/28180) — 7 comments · 0 reactions · closed
- **Pull Request** [\[metrics\] Add more useful metrics](https://github.com/sgl-project/sglang/pull/15809) — 11 comments · 1 reactions · closed

### [Ray](https://github.com/ray-project/ray)

- **Issue** [\[Serve\] Orphan ProxyActor left ALIVE when proxy shutdown times out under heavy controller load (blocks worker scale-down)](https://github.com/ray-project/ray/issues/64984) — 5 comments · 0 reactions · open
- **Issue** [\[Data\] Remove existing chaos and autoscaling release test variants](https://github.com/ray-project/ray/issues/65504) — 0 comments · 0 reactions · open
- **Pull Request** [\[core\]\[dashboard\] Return 4xx from node and actor detail APIs](https://github.com/ray-project/ray/pull/65015) — 4 comments · 1 reactions · open
- **Issue** [\[serve\] Unscheduleable replica shutdown is not handled gracefully](https://github.com/ray-project/ray/issues/50426) — 3 comments · 0 reactions · open
- **Issue** [\[core\] Unify executor threads when enabling/disabling concurrency_groups](https://github.com/ray-project/ray/issues/54639) — 2 comments · 0 reactions · open
- **Pull Request** [\[Serve\] Add serve deploy --merge for per application upsert](https://github.com/ray-project/ray/pull/63073) — 6 comments · 1 reactions · open
- **Pull Request** [\[Serve\] \[1/N\] Add RolloutSupervisor  core logic - auto-rollback feature](https://github.com/ray-project/ray/pull/63382) — 6 comments · 1 reactions · open
- **Pull Request** [\[jobs\] Simplify job submission failure stack traces](https://github.com/ray-project/ray/pull/64621) — 6 comments · 1 reactions · open
- **Pull Request** [\[Data\] Pin fused map function for shuffle tasks](https://github.com/ray-project/ray/pull/65480) — 2 comments · 1 reactions · open
- **Issue** [\[Serve\] jinja2 imported by haproxy.py but not declared by ray\[serve\] — slim installs can't import ray.serve](https://github.com/ray-project/ray/issues/65507) — 0 comments · 0 reactions · open
- **Issue** [\[Data\] Modify maximum memory to OOM prevention guidance](https://github.com/ray-project/ray/issues/65508) — 0 comments · 0 reactions · open
- **Issue** [\[Data\] Warn when configured memory is below 1.25x max USS](https://github.com/ray-project/ray/issues/65511) — 0 comments · 0 reactions · open
- **Issue** [\[core\]\[scheduler\] Iterator invalidation in node label scheduling filter](https://github.com/ray-project/ray/issues/65517) — 0 comments · 0 reactions · open
- **Pull Request** [\[Serve\] Add observability metrics for CapacityQueueRouter](https://github.com/ray-project/ray/pull/63014) — 5 comments · 1 reactions · open
- **Pull Request** [\[Data\]\[2/N\] add external shuffle task+operators](https://github.com/ray-project/ray/pull/65144) — 0 comments · 1 reactions · open
- **Pull Request** [\[Data\] OpTask._cancel never passes force=True](https://github.com/ray-project/ray/pull/65389) — 0 comments · 1 reactions · open
- **Pull Request** [\[doc\]\[KubeRay\] document ingressOptions for the built-in Ingress](https://github.com/ray-project/ray/pull/65483) — 1 comments · 1 reactions · open
- **Pull Request** [\[Core\] Add job level configuration to enable/disable lineage reconstruction](https://github.com/ray-project/ray/pull/65487) — 0 comments · 1 reactions · open
- **Pull Request** [\[Docs\]\[KubeRay\] Update all KubeRay version references to 1.7.0](https://github.com/ray-project/ray/pull/65498) — 1 comments · 1 reactions · open
- **Pull Request** [\[Data\]\[3/n\] external shuffle planner](https://github.com/ray-project/ray/pull/65499) — 0 comments · 1 reactions · open
- **Pull Request** [add initial documentation for Ray sandboxing](https://github.com/ray-project/ray/pull/65503) — 0 comments · 1 reactions · open
- **Pull Request** [\[Docs\]\[KubeRay\] Use RayJob sample YAML for History Server docs](https://github.com/ray-project/ray/pull/65505) — 1 comments · 1 reactions · open
- **Pull Request** [\[Core\] Fix recovery suppression race in ObjectRecoveryManager](https://github.com/ray-project/ray/pull/64974) — 2 comments · 1 reactions · open
- **Pull Request** [\[core\] fix None yield from restarted streaming generator with application errors](https://github.com/ray-project/ray/pull/65121) — 1 comments · 1 reactions · open
- **Pull Request** [\[Data\] Async generator map_batches UDFs ignore target_max_block_size; peak scales with yields per call](https://github.com/ray-project/ray/pull/65162) — 1 comments · 1 reactions · open
- **Pull Request** [\[Data\] Remove chaos and autoscaling release test variants](https://github.com/ray-project/ray/pull/65506) — 0 comments · 1 reactions · open
- **Pull Request** [\[Data\] Modify maximum memory to OOM prevention docs](https://github.com/ray-project/ray/pull/65509) — 1 comments · 1 reactions · open
- **Pull Request** [\[cherry-pick\]\[2.58.0\]\[doc\]\[History server\] Update doc for history server for `RAY_ROOT_DIR` -> `STORAGE_ROOT_DIR` (#65441)](https://github.com/ray-project/ray/pull/65510) — 0 comments · 1 reactions · closed
- **Pull Request** [\[Data\] Warn when configured memory is below 1.25x max USS](https://github.com/ray-project/ray/pull/65512) — 1 comments · 1 reactions · open
- **Pull Request** [\[Doc\] Fix docs for KubeRay v1.7](https://github.com/ray-project/ray/pull/65513) — 0 comments · 1 reactions · open

### [BentoML](https://github.com/bentoml/BentoML)

- **Pull Request** [fix: preserve latin-1 response header bytes in task result serde](https://github.com/bentoml/BentoML/pull/5693) — 0 comments · 0 reactions · open
- **Pull Request** [fix: mark task FAILED and persist a 500 response when the endpoint raises](https://github.com/bentoml/BentoML/pull/5694) — 0 comments · 0 reactions · open
- **Pull Request** [fix: stop cancel_task from wedging the task row in a half-canceled state](https://github.com/bentoml/BentoML/pull/5695) — 0 comments · 0 reactions · open
