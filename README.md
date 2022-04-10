# proto-buf-python

Protocol buffers (Protobuf) are a language-agnostic data serialization format developed by Google.

   **Low data volume:** Protobuf makes use of a binary format, which is more compact than other formats such as JSON.
   
   **Persistence:** Protobuf serialization is backward-compatible. This means that you can always restore previous data, even if the interfaces have changed in the meantime.
   
   **Design by contract:** Protobuf requires the specification of messages using explicit identifiers and types.
   
   **Requirement for gRPC:** gRPC (gRPC Remote Procedure Call) is an efficient remote procedure call system that makes use of the Protobuf format.
   
