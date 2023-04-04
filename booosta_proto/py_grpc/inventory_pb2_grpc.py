# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from booosta_proto.py_grpc import inventory_pb2 as inventory__pb2


class InventoryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetProductInventoryById = channel.unary_unary(
                '/inventory.InventoryService/GetProductInventoryById',
                request_serializer=inventory__pb2.GetProductInventoryByIdRequest.SerializeToString,
                response_deserializer=inventory__pb2.GetProductInventoryByIdResponse.FromString,
                )
        self.GetUnitTypeById = channel.unary_unary(
                '/inventory.InventoryService/GetUnitTypeById',
                request_serializer=inventory__pb2.GetUnitTypeByIdRequest.SerializeToString,
                response_deserializer=inventory__pb2.GetUnitTypeByIdResponse.FromString,
                )
        self.GetProductInventoryByUserIDAndQuantity = channel.unary_unary(
                '/inventory.InventoryService/GetProductInventoryByUserIDAndQuantity',
                request_serializer=inventory__pb2.GetProductInventoryByUserIDAndQuantityRequest.SerializeToString,
                response_deserializer=inventory__pb2.GetProductInventoryByUserIDAndQuantityResponse.FromString,
                )
        self.GetRetailerProductList = channel.unary_unary(
                '/inventory.InventoryService/GetRetailerProductList',
                request_serializer=inventory__pb2.GetRetailerProductListRequest.SerializeToString,
                response_deserializer=inventory__pb2.GetRetailerProductListResponse.FromString,
                )


class InventoryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetProductInventoryById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUnitTypeById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProductInventoryByUserIDAndQuantity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRetailerProductList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InventoryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetProductInventoryById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProductInventoryById,
                    request_deserializer=inventory__pb2.GetProductInventoryByIdRequest.FromString,
                    response_serializer=inventory__pb2.GetProductInventoryByIdResponse.SerializeToString,
            ),
            'GetUnitTypeById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUnitTypeById,
                    request_deserializer=inventory__pb2.GetUnitTypeByIdRequest.FromString,
                    response_serializer=inventory__pb2.GetUnitTypeByIdResponse.SerializeToString,
            ),
            'GetProductInventoryByUserIDAndQuantity': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProductInventoryByUserIDAndQuantity,
                    request_deserializer=inventory__pb2.GetProductInventoryByUserIDAndQuantityRequest.FromString,
                    response_serializer=inventory__pb2.GetProductInventoryByUserIDAndQuantityResponse.SerializeToString,
            ),
            'GetRetailerProductList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRetailerProductList,
                    request_deserializer=inventory__pb2.GetRetailerProductListRequest.FromString,
                    response_serializer=inventory__pb2.GetRetailerProductListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'inventory.InventoryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InventoryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetProductInventoryById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inventory.InventoryService/GetProductInventoryById',
            inventory__pb2.GetProductInventoryByIdRequest.SerializeToString,
            inventory__pb2.GetProductInventoryByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUnitTypeById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inventory.InventoryService/GetUnitTypeById',
            inventory__pb2.GetUnitTypeByIdRequest.SerializeToString,
            inventory__pb2.GetUnitTypeByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProductInventoryByUserIDAndQuantity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inventory.InventoryService/GetProductInventoryByUserIDAndQuantity',
            inventory__pb2.GetProductInventoryByUserIDAndQuantityRequest.SerializeToString,
            inventory__pb2.GetProductInventoryByUserIDAndQuantityResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRetailerProductList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inventory.InventoryService/GetRetailerProductList',
            inventory__pb2.GetRetailerProductListRequest.SerializeToString,
            inventory__pb2.GetRetailerProductListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
