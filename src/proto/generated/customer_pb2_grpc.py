# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import customer_pb2 as customer__pb2


class CustomerDetailsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_customer = channel.unary_unary(
                '/customer.CustomerDetails/get_customer',
                request_serializer=customer__pb2.Customer.SerializeToString,
                response_deserializer=customer__pb2.Reply.FromString,
                )


class CustomerDetailsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_customer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CustomerDetailsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_customer': grpc.unary_unary_rpc_method_handler(
                    servicer.get_customer,
                    request_deserializer=customer__pb2.Customer.FromString,
                    response_serializer=customer__pb2.Reply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'customer.CustomerDetails', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CustomerDetails(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_customer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/customer.CustomerDetails/get_customer',
            customer__pb2.Customer.SerializeToString,
            customer__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
