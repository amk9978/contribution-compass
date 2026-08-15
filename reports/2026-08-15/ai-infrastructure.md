# AI Infrastructure — 2026-08-15

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [\[Roadmap\] sglang auto tuner](https://github.com/sgl-project/sglang/issues/13363)

- Project: `sgl-project/sglang`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: good first issue; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [\[Data\] write_lance is incompatible with PyLance 6.x due to removed storage_options_provider argument](https://github.com/ray-project/ray/issues/65129)

- Project: `ray-project/ray`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: good first issue; No assignee is listed
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

## Important Updates

### [LiteLLM](https://github.com/BerriAI/litellm)

- **Issue** [\[Feature\]: Dark Mode](https://github.com/BerriAI/litellm/issues/10177) — 63 comments · 84 reactions · open
- **Issue** [\[Feature\]: Auto-populate max_input_tokens/max_output_tokens for hosted vLLM/OpenAI-like models](https://github.com/BerriAI/litellm/issues/27830) — 2 comments · 6 reactions · open
- **Issue** [\[Bug\]: Latest stable 1.81.14 fails on thinking and tools](https://github.com/BerriAI/litellm/issues/22997) — 5 comments · 4 reactions · closed
- **Pull Request** [feat(auto-router): scope shadow eval jobs to multiple keys](https://github.com/BerriAI/litellm/pull/36871) — 21 comments · 1 reactions · open
- **Pull Request** [fix(s3_v2): URL-encode object keys to prevent SigV4 signature mismatch](https://github.com/BerriAI/litellm/pull/24585) — 8 comments · 3 reactions · open
- **Pull Request** [Fix DeepSeek V4 reasoning_content in multi-turn chat](https://github.com/BerriAI/litellm/pull/26678) — 8 comments · 4 reactions · closed
- **Pull Request** [feat(fireworks_ai): translate NIM/vLLM extra params to Fireworks-native args](https://github.com/BerriAI/litellm/pull/35969) — 14 comments · 1 reactions · closed
- **Pull Request** [fix(azure_ai): recognize real Search doc endpoints so teams can read/write via passthrough](https://github.com/BerriAI/litellm/pull/33757) — 12 comments · 1 reactions · closed
- **Pull Request** [fix(ui): match auto-router preset models against the model groups the tier dropdown lists](https://github.com/BerriAI/litellm/pull/36440) — 17 comments · 1 reactions · closed
- **Pull Request** [fix(proxy): requeue spend logs when the DB write fails with a transport error](https://github.com/BerriAI/litellm/pull/36716) — 13 comments · 1 reactions · open
- **Pull Request** [feat(shadow_eval): add reverse-direction shadow eval jobs](https://github.com/BerriAI/litellm/pull/36865) — 12 comments · 1 reactions · closed
- **Issue** [Mid-conversation system-role hoist invalidates the entire prompt-cache prefix (AnthropicMessagesConfig)](https://github.com/BerriAI/litellm/issues/36559) — 7 comments · 0 reactions · open
- **Pull Request** [Cache Azure token providers](https://github.com/BerriAI/litellm/pull/24424) — 11 comments · 1 reactions · open
- **Pull Request** [fix(anthropic_messages): make tool_result images visible to OpenAI-compatible providers](https://github.com/BerriAI/litellm/pull/34462) — 10 comments · 1 reactions · closed
- **Pull Request** [feat(providers): add SCX.ai as a JSON-configured OpenAI-compatible provider](https://github.com/BerriAI/litellm/pull/34752) — 10 comments · 1 reactions · open
- **Pull Request** [fix(proxy): force prisma recreate on postgres cached-plan error](https://github.com/BerriAI/litellm/pull/36428) — 10 comments · 1 reactions · closed
- **Pull Request** [fix(cost): tiered pricing supports cache creation cost and is all-or-nothing](https://github.com/BerriAI/litellm/pull/36720) — 11 comments · 1 reactions · open
- **Pull Request** [feat(mcp): clear and reauthorize a server's stored MCP OAuth tokens](https://github.com/BerriAI/litellm/pull/36831) — 10 comments · 1 reactions · open
- **Pull Request** [fix(azure): rename max_tokens to max_completion_tokens for gpt-5-chat deployments](https://github.com/BerriAI/litellm/pull/36857) — 10 comments · 1 reactions · open
- **Pull Request** [fix(mcp): keep admin-entered oauth endpoints in management reads](https://github.com/BerriAI/litellm/pull/36888) — 10 comments · 1 reactions · closed
- **Pull Request** [feat(proxy): per-component response cost headers](https://github.com/BerriAI/litellm/pull/36965) — 10 comments · 1 reactions · closed
- **Pull Request** [VLLM: Prevent side-channel attacks via cache salting (CVE-2025-46570)](https://github.com/BerriAI/litellm/pull/27925) — 9 comments · 1 reactions · open
- **Pull Request** [fix(vertex_ai): translate /v1/embeddings batch rows to the Gemini embedding shape](https://github.com/BerriAI/litellm/pull/35092) — 12 comments · 1 reactions · open
- **Pull Request** [fix(datadog_llm_obs): map tool_calls to DD Message schema and cache tokens to span metrics](https://github.com/BerriAI/litellm/pull/35946) — 8 comments · 1 reactions · open
- **Pull Request** [fix(azure_ai): recognize real Search doc endpoints so teams can read/write via passthrough](https://github.com/BerriAI/litellm/pull/36798) — 8 comments · 1 reactions · closed
- **Pull Request** [feat(bedrock): forward LiteLLM identity and metadata into Bedrock requestMetadata](https://github.com/BerriAI/litellm/pull/36861) — 8 comments · 1 reactions · open
- **Pull Request** [fix(langfuse): restrict trace steering keys to real langfuse trace fields](https://github.com/BerriAI/litellm/pull/36862) — 8 comments · 1 reactions · closed
- **Pull Request** [fix(mcp): drop caller host and configured upstream headers from logged metadata](https://github.com/BerriAI/litellm/pull/36901) — 8 comments · 1 reactions · closed
- **Pull Request** [fix(proxy): prevent false BudgetExceededError after global proxy budget reset](https://github.com/BerriAI/litellm/pull/36953) — 8 comments · 1 reactions · open
- **Issue** [\[Feature\]: Support Ollama text-to-image via litellm.image_generation (x/flux2-klein etc.)](https://github.com/BerriAI/litellm/issues/28026) — 2 comments · 0 reactions · open

### [vLLM](https://github.com/vllm-project/vllm)

- **Pull Request** [\[Model\] Add Inkling multi-depth MTP support \[5/N\]](https://github.com/vllm-project/vllm/pull/48768) — 8 comments · 14 reactions · closed
- **Pull Request** [\[Core\] Extensible (growable) KV cache](https://github.com/vllm-project/vllm/pull/50779) — 22 comments · 5 reactions · open
- **Pull Request** [refactor(envs): migrate vllm/envs.py to pydantic-settings](https://github.com/vllm-project/vllm/pull/42136) — 29 comments · 3 reactions · open
- **Pull Request** [\[MoE\] Generalize masked activation for padded layouts](https://github.com/vllm-project/vllm/pull/51217) — 14 comments · 2 reactions · open
- **Pull Request** [\[Core\] Check for GPU<->CPU syncs during CI](https://github.com/vllm-project/vllm/pull/43107) — 31 comments · 3 reactions · closed
- **Pull Request** [\[Bugfix\]\[CI\] Retry cached HF tokenizer load after transport failures](https://github.com/vllm-project/vllm/pull/44820) — 9 comments · 2 reactions · closed
- **Pull Request** [\[Kernel\] Add native CUDA fused RoPE + KV cache write op, opt-in for flash_attn](https://github.com/vllm-project/vllm/pull/43355) — 6 comments · 3 reactions · closed
- **Pull Request** [\[ROCm\]\[CI\] Gating more ROCm tests](https://github.com/vllm-project/vllm/pull/44969) — 29 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\] Add Kimi K3 MoE support to benchmark_moe.py](https://github.com/vllm-project/vllm/pull/50082) — 4 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\] Fix speculative decoding for short_conv (LFM2) models](https://github.com/vllm-project/vllm/pull/50272) — 21 comments · 4 reactions · open
- **Pull Request** [\[Kernel\]\[Model\] Add manual CUDA RoPE KV-cache fusion for Llama](https://github.com/vllm-project/vllm/pull/52363) — 4 comments · 2 reactions · open
- **Pull Request** [\[K3\] support recoverssm for K3](https://github.com/vllm-project/vllm/pull/51855) — 3 comments · 2 reactions · open
- **Pull Request** [Feat/spec decode under pipeline parallel](https://github.com/vllm-project/vllm/pull/50514) — 24 comments · 2 reactions · open
- **Pull Request** [\[ModelRunnerV2\] Support prompt embeds](https://github.com/vllm-project/vllm/pull/42963) — 19 comments · 3 reactions · open
- **Pull Request** [\[Bugfix\] Make DSV4 sparse MLA work end-to-end for plain decode, MTP, and DSpark](https://github.com/vllm-project/vllm/pull/51538) — 23 comments · 2 reactions · open
- **Pull Request** [\[6/N\]\[KV-Cache Layout Refactor\] Standardize KV cache layout](https://github.com/vllm-project/vllm/pull/51718) — 6 comments · 0 reactions · open
- **Pull Request** [\[Core\] Use FlashInfer workspace sizing helper](https://github.com/vllm-project/vllm/pull/46883) — 18 comments · 2 reactions · open
- **Pull Request** [\[EC Connector\] Added Build Connector Worker Meta for EC Connector](https://github.com/vllm-project/vllm/pull/49585) — 18 comments · 2 reactions · open
- **Issue** [\[RFC\]: O(1) KV Cache for vLLM: 4.8x Speedup & 22x More Accurate than TurboQuant on Qwen2.5-7B](https://github.com/vllm-project/vllm/issues/38694) — 4 comments · 4 reactions · closed
- **Issue** [\[Feature\]: Kimi K3 Performance Optimization](https://github.com/vllm-project/vllm/issues/50587) — 0 comments · 4 reactions · open
- **Issue** [\[ROCm\]\[AMD\] Kimi-K3 Gap and Roadmap Tracking](https://github.com/vllm-project/vllm/issues/50682) — 17 comments · 0 reactions · open
- **Pull Request** [\[Kimi-K3\]\[AMD\] Return KDA and MLA projection outputs directly](https://github.com/vllm-project/vllm/pull/50592) — 16 comments · 2 reactions · open
- **Issue** [\[RFC\]: Standardize vLLM Entrypoint Error Handling](https://github.com/vllm-project/vllm/issues/48227) — 10 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\] Ensure DeepGEMM metadata gets contiguous context_lens](https://github.com/vllm-project/vllm/pull/40989) — 10 comments · 3 reactions · open
- **Pull Request** [\[Frontend\]  Support count_reasoning_tokens in the Streaming Parser Engine](https://github.com/vllm-project/vllm/pull/45802) — 14 comments · 2 reactions · open
- **Pull Request** [\[Core\] Use FlashInfer for pre-SM100 NVFP4 KV cache updates](https://github.com/vllm-project/vllm/pull/46963) — 14 comments · 2 reactions · open
- **Pull Request** [\[Frontend\]\[Core\]\[Spec Decode\] Per-request acceptance stats in OpenAI API responses](https://github.com/vllm-project/vllm/pull/48915) — 15 comments · 2 reactions · open
- **Pull Request** [\[Spec Decode\]\[Perf\] Fuse the MTP trailing all-reduce; local-argmax draft tokens](https://github.com/vllm-project/vllm/pull/49793) — 15 comments · 2 reactions · closed
- **Pull Request** [\[Bugfix\]\[Mooncake\] Save exact Mamba boundary states](https://github.com/vllm-project/vllm/pull/51358) — 2 comments · 5 reactions · open
- **Pull Request** [\[Feature\] Support batch invariance on ROCm](https://github.com/vllm-project/vllm/pull/52231) — 7 comments · 4 reactions · open

### [SGLang](https://github.com/sgl-project/sglang)

- **Issue** [\[Roadmap\] Context Parallelism  (2026 Q3)](https://github.com/sgl-project/sglang/issues/21788) — 22 comments · 16 reactions · open
- **Issue** [\[Tracking\] CI Test Failures and Fixes](https://github.com/sgl-project/sglang/issues/17050) — 13 comments · 10 reactions · open
- **Issue** [\[RFC\] Sglang non-GPU process rust migration](https://github.com/sgl-project/sglang/issues/23206) — 6 comments · 11 reactions · open
- **Pull Request** [\[P/D disagg\] Decode-side radix cache for SWA hybrid models (unified radix tree)](https://github.com/sgl-project/sglang/pull/27770) — 40 comments · 3 reactions · open
- **Pull Request** [\[HiCache\] Dedup MLA KV cache in host memory across TP ranks](https://github.com/sgl-project/sglang/pull/26691) — 13 comments · 7 reactions · open
- **Pull Request** [\[AMD\]\[Quantization\] Online MXFP4 quantization 4/N - NVFP4 to MXFP4 Online Requantization on AMD GPUs](https://github.com/sgl-project/sglang/pull/29328) — 24 comments · 1 reactions · open
- **Issue** [\[Roadmap\]\[DCP\] Decode Context Parallelism & Helix Parallelism (2026 Q3)](https://github.com/sgl-project/sglang/issues/29736) — 13 comments · 2 reactions · open
- **Pull Request** [\[NVIDIA\]\[comm\] Merge EP+MoE-TP post-experts all-reduces into one _TP reduction](https://github.com/sgl-project/sglang/pull/32963) — 22 comments · 0 reactions · open
- **Issue** [\[Bug\] \[Diffusion\] Attention backend fallback change introduced errors on most models](https://github.com/sgl-project/sglang/issues/34389) — 7 comments · 0 reactions · open
- **Pull Request** [Support TP overlap on Blackwell](https://github.com/sgl-project/sglang/pull/15103) — 11 comments · 2 reactions · closed
- **Pull Request** [\[NPU\] Add mxfp4-w4a8 MOE Quantization Support for NPU](https://github.com/sgl-project/sglang/pull/30318) — 15 comments · 0 reactions · open
- **Pull Request** [\[FP8\]\[MoE\] Honor UE8M0 activation scales in Triton MoE](https://github.com/sgl-project/sglang/pull/33005) — 14 comments · 0 reactions · open
- **Pull Request** [Return expert routing info to support MoE routing replay](https://github.com/sgl-project/sglang/pull/9499) — 11 comments · 2 reactions · closed
- **Pull Request** [\[DSA\] Skip indexer KV cache for skip-topk layers](https://github.com/sgl-project/sglang/pull/30531) — 13 comments · 0 reactions · open
- **Pull Request** [\[GDN\] Add MTP cache mode for final-state recompute, with FlashInfer kernel integration and overlapped CUDA-graph state recovery](https://github.com/sgl-project/sglang/pull/30967) — 8 comments · 1 reactions · open
- **Pull Request** [fix(bcg): preserve Qwen3-VL DeepStack inputs during replay](https://github.com/sgl-project/sglang/pull/33726) — 12 comments · 0 reactions · open
- **Pull Request** [\[AMD\] Enable Fast Triton Sparse MLA backend](https://github.com/sgl-project/sglang/pull/30575) — 7 comments · 1 reactions · open
- **Pull Request** [Support mixed MXFP8 and NVFP4 modelopt checkpoints](https://github.com/sgl-project/sglang/pull/31282) — 11 comments · 0 reactions · open
- **Issue** [\[Bug\] flashinfer_trtllm MoE runner corrupts MiniMax-M2.7-NVFP4 output and asserts on DeepSeek-V4-Flash on B200](https://github.com/sgl-project/sglang/issues/26324) — 5 comments · 0 reactions · closed
- **Issue** [\[Bug\] DeepSeek-V4-Flash on GB200 aborts during startup with duplicate TVM FFI registration](https://github.com/sgl-project/sglang/issues/34858) — 1 comments · 0 reactions · closed
- **Pull Request** [OpenVLA Support](https://github.com/sgl-project/sglang/pull/10763) — 5 comments · 2 reactions · closed
- **Pull Request** [\[Diffusion\] Unify component residency controls](https://github.com/sgl-project/sglang/pull/34736) — 8 comments · 0 reactions · open
- **Issue** [\[Bug\] Intermittent NCCL hang during Spec V2 verify with DSA backend + HiCache (post PR #18958 fix)](https://github.com/sgl-project/sglang/issues/28011) — 3 comments · 0 reactions · closed
- **Pull Request** [perf(sgl-kernel): default block_quota=16 for MLA page_first KV gather…](https://github.com/sgl-project/sglang/pull/30024) — 3 comments · 1 reactions · open
- **Pull Request** [\[ray\] Support Ray metric backend for engine metrics](https://github.com/sgl-project/sglang/pull/31415) — 11 comments · 0 reactions · open
- **Pull Request** [\[XPU\] upgrade sglang xpu backend to PyTorch 2.13](https://github.com/sgl-project/sglang/pull/31751) — 7 comments · 0 reactions · open
- **Pull Request** [fix(dsa): use FlashInfer fused top-k for packed PAGED rows](https://github.com/sgl-project/sglang/pull/33006) — 7 comments · 0 reactions · closed
- **Pull Request** [\[Spec\] Support mamba-radix-cache-strategy extra_buffer_lazy with DFLASH](https://github.com/sgl-project/sglang/pull/34763) — 6 comments · 0 reactions · open
- **Pull Request** [\[AMD\]\[CI\] Fix stage-b: AttributeError on multimodal embedding requests](https://github.com/sgl-project/sglang/pull/34769) — 6 comments · 0 reactions · open
- **Pull Request** [\[Fix\] Handle aborts before assembling streaming logprobs in OpenAI endpoints](https://github.com/sgl-project/sglang/pull/34776) — 7 comments · 0 reactions · open

### [Ray](https://github.com/ray-project/ray)

- **Issue** [\[Serve\] performance bottlenecked by the ProxyActor](https://github.com/ray-project/ray/issues/42565) — 13 comments · 10 reactions · closed
- **Issue** [\[serve\]\[llm\] Governance middleware layer for Ray Serve LLM — PII detection, cost budgets, policy enforcement, and audit trails](https://github.com/ray-project/ray/issues/65259) — 9 comments · 0 reactions · open
- **Issue** [\[serve\]\[llm\] s3:// model_source is dropped on Ray 2.57.0: engine config gets model_id instead of the staged local path](https://github.com/ray-project/ray/issues/65477) — 0 comments · 0 reactions · open
- **Issue** [\[Security\] Private vulnerability reports are being acted on without any response to the reporter](https://github.com/ray-project/ray/issues/65367) — 3 comments · 0 reactions · open
- **Pull Request** [\[serve\] Columnar zero-copy autoscaling-metrics ingest](https://github.com/ray-project/ray/pull/64281) — 2 comments · 1 reactions · open
- **Issue** [\[Umbrella\] Ray Sandboxing with gVisor](https://github.com/ray-project/ray/issues/65352) — 9 comments · 3 reactions · open
- **Pull Request** [\[Data\] Support appending a subset of columns to a Lance dataset.](https://github.com/ray-project/ray/pull/64474) — 4 comments · 1 reactions · open
- **Pull Request** [\[Data\] Add DataIterator.count() to get dataset/shard size](https://github.com/ray-project/ray/pull/64869) — 4 comments · 1 reactions · open
- **Pull Request** [\[core\] Free local objects batching](https://github.com/ray-project/ray/pull/65000) — 1 comments · 2 reactions · closed
- **Pull Request** [\[jobs\]: return structured 503 when job logs are unavailable](https://github.com/ray-project/ray/pull/65405) — 4 comments · 1 reactions · open
- **Issue** [\[tune\] Optuna must be installed! error despite having optuna installed](https://github.com/ray-project/ray/issues/65376) — 2 comments · 0 reactions · closed
- **Pull Request** [\[Data\] Disallow min_rows_per_file with partitioned parquet writes](https://github.com/ray-project/ray/pull/63368) — 3 comments · 1 reactions · open
- **Pull Request** [\[Data\] Fix ResourceBudget backpressure causing pipeline stall](https://github.com/ray-project/ray/pull/64601) — 3 comments · 1 reactions · open
- **Pull Request** [\[Serve\] Optimize RollingWindow metrics using monotonic deque in O(1)](https://github.com/ray-project/ray/pull/65031) — 3 comments · 1 reactions · open
- **Pull Request** [\[llm\]\[ci\] Upgrade to vllm 0.27.0](https://github.com/ray-project/ray/pull/65351) — 2 comments · 1 reactions · open
- **Pull Request** [\[Data\]\[LLM\] Add multi-host TPU batch inference for Ray Data LLM](https://github.com/ray-project/ray/pull/65422) — 3 comments · 1 reactions · open
- **Pull Request** [\[Data\] Add support for writing ORC files](https://github.com/ray-project/ray/pull/65453) — 2 comments · 1 reactions · open
- **Pull Request** [\[docs\] Convert the seven card-grid library front doors from RST to MyST](https://github.com/ray-project/ray/pull/65470) — 2 comments · 1 reactions · closed
- **Issue** [\[Data\] write_lance is incompatible with PyLance 6.x due to removed storage_options_provider argument](https://github.com/ray-project/ray/issues/65129) — 1 comments · 0 reactions · open
- **Issue** [\[core\] Support dynamically force-inlining objects larger than the size threshold](https://github.com/ray-project/ray/issues/65490) — 0 comments · 0 reactions · open
- **Pull Request** [\[Data\] Support Arrow string-view and binary-view arrays in custom serialization](https://github.com/ray-project/ray/pull/64801) — 4 comments · 1 reactions · closed
- **Pull Request** [\[core\] Isolate NodeInfoGcsService.GetClusterId on a dedicated lightweight-reads io_context](https://github.com/ray-project/ray/pull/64845) — 4 comments · 1 reactions · open
- **Pull Request** [\[Data\] Support predicate pushdown at the Delta Lake level](https://github.com/ray-project/ray/pull/65142) — 5 comments · 1 reactions · open
- **Pull Request** [\[Data\] \[5/11\] Add the Parquet FooterReader actor pool](https://github.com/ray-project/ray/pull/65273) — 1 comments · 1 reactions · open
- **Pull Request** [\[doc\] Update the number of index.rst document](https://github.com/ray-project/ray/pull/65363) — 1 comments · 1 reactions · open
- **Pull Request** [\[Data\] Update docs for hash shuffle v2](https://github.com/ray-project/ray/pull/65372) — 1 comments · 1 reactions · open
- **Pull Request** [\[serve\] Add separate fast path for unary gRPC direct ingress](https://github.com/ray-project/ray/pull/65398) — 0 comments · 1 reactions · open
- **Pull Request** [\[core\] Tombstone lease ids on CancelWorkerLease](https://github.com/ray-project/ray/pull/65420) — 0 comments · 1 reactions · closed
- **Pull Request** [\[ci\] Scope the doc_readme lint check to the files it actually checks](https://github.com/ray-project/ray/pull/65431) — 0 comments · 1 reactions · closed
- **Pull Request** [\[serve\]\[llm\] Surface engine errors on the direct-streaming ASGI app](https://github.com/ray-project/ray/pull/65440) — 0 comments · 1 reactions · closed

### [BentoML](https://github.com/bentoml/BentoML)

No new or materially changed signals.
