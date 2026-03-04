# RAG Pipeline FAQ

## Q: What are the core stages of RAG?
A: Ingestion, chunking, embedding, indexing, retrieval, reranking, and grounded generation.

## Q: What chunk size should we start with?
A: Start with 400-800 tokens and tune based on retrieval precision and context limits.

## Q: Why use metadata filters?
A: Filters improve retrieval precision by limiting results to relevant product, version, or team docs.

## Q: How do we reduce hallucinations in RAG?
A: Use strong retrieval, enforce citations, and return 'insufficient evidence' when confidence is low.

## Q: What retrieval strategy works best?
A: Hybrid retrieval (vector + keyword) often performs better than single-mode retrieval.
