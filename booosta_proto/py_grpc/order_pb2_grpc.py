# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from booosta_proto.py_grpc import order_pb2 as order__pb2


class OrderServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetOrderById = channel.unary_unary(
                '/order.OrderService/GetOrderById',
                request_serializer=order__pb2.GetOrderByIdRequest.SerializeToString,
                response_deserializer=order__pb2.GetOrderByIdResponse.FromString,
                )
        self.GetOrderItemById = channel.unary_unary(
                '/order.OrderService/GetOrderItemById',
                request_serializer=order__pb2.GetOrderItemByIdRequest.SerializeToString,
                response_deserializer=order__pb2.GetOrderItemByIdResponse.FromString,
                )
        self.GetOrderItemsByProductId = channel.unary_unary(
                '/order.OrderService/GetOrderItemsByProductId',
                request_serializer=order__pb2.GetOrderItemsByProductIdRequest.SerializeToString,
                response_deserializer=order__pb2.GetOrderItemsByProductIdResponse.FromString,
                )


class OrderServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetOrderById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrderItemById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrderItemsByProductId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetOrderById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrderById,
                    request_deserializer=order__pb2.GetOrderByIdRequest.FromString,
                    response_serializer=order__pb2.GetOrderByIdResponse.SerializeToString,
            ),
            'GetOrderItemById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrderItemById,
                    request_deserializer=order__pb2.GetOrderItemByIdRequest.FromString,
                    response_serializer=order__pb2.GetOrderItemByIdResponse.SerializeToString,
            ),
            'GetOrderItemsByProductId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrderItemsByProductId,
                    request_deserializer=order__pb2.GetOrderItemsByProductIdRequest.FromString,
                    response_serializer=order__pb2.GetOrderItemsByProductIdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'order.OrderService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OrderService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetOrderById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/order.OrderService/GetOrderById',
            order__pb2.GetOrderByIdRequest.SerializeToString,
            order__pb2.GetOrderByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrderItemById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/order.OrderService/GetOrderItemById',
            order__pb2.GetOrderItemByIdRequest.SerializeToString,
            order__pb2.GetOrderItemByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrderItemsByProductId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/order.OrderService/GetOrderItemsByProductId',
            order__pb2.GetOrderItemsByProductIdRequest.SerializeToString,
            order__pb2.GetOrderItemsByProductIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)