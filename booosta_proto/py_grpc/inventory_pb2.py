# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventory.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0finventory.proto\x12\tinventory\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\"\xa1\x02\n\x10ProductInventory\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\ncost_price\x18\x03 \x01(\x02\x12\x18\n\x10\x63urrent_quantity\x18\x04 \x01(\x03\x12\x1e\n\x16minimum_stock_quantity\x18\x05 \x01(\x03\x12\x15\n\rcreated_by_id\x18\x06 \x01(\t\x12\r\n\x05image\x18\x07 \x01(\t\x12\x18\n\x10\x64\x65\x66\x61ult_quantity\x18\x08 \x01(\x03\x12\x11\n\tunit_type\x18\t \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\n \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x0b \x01(\t\x12\x14\n\x0clow_quantity\x18\x0c \x01(\x08\x12\x15\n\rselling_price\x18\r \x01(\x02\"\xb8\x02\n\x10ProductAdminList\x12\x16\n\x0estock_quantity\x18\x01 \x01(\x03\x12\x13\n\x0bstock_value\x18\x02 \x01(\x03\x12\x0c\n\x04sold\x18\x03 \x01(\x03\x12\x0e\n\x06status\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\x02\x12\x15\n\rbusiness_name\x18\x06 \x01(\t\x12\x12\n\ncost_price\x18\x07 \x01(\x02\x12\n\n\x02id\x18\x08 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\t \x01(\t\x12\x1e\n\x16minimum_stock_quantity\x18\n \x01(\x03\x12\x18\n\x10\x64\x65\x66\x61ult_quantity\x18\x0b \x01(\x03\x12\x0c\n\x04name\x18\x0c \x01(\t\x12.\n\ncreated_at\x18\r \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x18\n\x08UnitType\x12\x0c\n\x04name\x18\x01 \x01(\t\",\n\x1eGetProductInventoryByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"$\n\x16GetUnitTypeByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"Y\n\x1fGetProductInventoryByIdResponse\x12\x36\n\x11product_inventory\x18\x01 \x01(\x0b\x32\x1b.inventory.ProductInventory\"A\n\x17GetUnitTypeByIdResponse\x12&\n\tunit_type\x18\x01 \x01(\x0b\x32\x13.inventory.UnitType\"\\\n-GetProductInventoryByUserIDAndQuantityRequest\x12\x15\n\rcreated_by_id\x18\x01 \x01(\t\x12\x14\n\x0clow_quantity\x18\x02 \x01(\x08\"T\n\"ChangeProductInventoryCountRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x63hange_type\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x03\"V\n\x1cProductInventoryListResponse\x12\x36\n\x11product_inventory\x18\x01 \x03(\x0b\x32\x1b.inventory.ProductInventory\";\n\"GetProductInventoryByUserIdRequest\x12\x15\n\rcreated_by_id\x18\x01 \x01(\t\"X\n\x1dGetRetailerProductListRequest\x12\x15\n\rcreated_by_id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x10\n\x08ordering\x18\x03 \x01(\t\"X\n\x1eGetRetailerProductListResponse\x12\x36\n\x11product_inventory\x18\x01 \x03(\x0b\x32\x1b.inventory.ProductAdminList2\xb7\x06\n\x10InventoryService\x12r\n\x17GetProductInventoryById\x12).inventory.GetProductInventoryByIdRequest\x1a*.inventory.GetProductInventoryByIdResponse\"\x00\x12Z\n\x0fGetUnitTypeById\x12!.inventory.GetUnitTypeByIdRequest\x1a\".inventory.GetUnitTypeByIdResponse\"\x00\x12\x8d\x01\n&GetProductInventoryByUserIDAndQuantity\x12\x38.inventory.GetProductInventoryByUserIDAndQuantityRequest\x1a\'.inventory.ProductInventoryListResponse\"\x00\x12w\n\x1bGetProductInventoryByUserId\x12-.inventory.GetProductInventoryByUserIdRequest\x1a\'.inventory.ProductInventoryListResponse\"\x00\x12o\n\x16GetRetailerProductList\x12(.inventory.GetRetailerProductListRequest\x1a).inventory.GetRetailerProductListResponse\"\x00\x12]\n\x18GetAllProductInventories\x12\x16.google.protobuf.Empty\x1a\'.inventory.ProductInventoryListResponse\"\x00\x12z\n\x1b\x43hangeProductInventoryCount\x12-.inventory.ChangeProductInventoryCountRequest\x1a*.inventory.GetProductInventoryByIdResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inventory_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PRODUCTINVENTORY._serialized_start=93
  _PRODUCTINVENTORY._serialized_end=382
  _PRODUCTADMINLIST._serialized_start=385
  _PRODUCTADMINLIST._serialized_end=697
  _UNITTYPE._serialized_start=699
  _UNITTYPE._serialized_end=723
  _GETPRODUCTINVENTORYBYIDREQUEST._serialized_start=725
  _GETPRODUCTINVENTORYBYIDREQUEST._serialized_end=769
  _GETUNITTYPEBYIDREQUEST._serialized_start=771
  _GETUNITTYPEBYIDREQUEST._serialized_end=807
  _GETPRODUCTINVENTORYBYIDRESPONSE._serialized_start=809
  _GETPRODUCTINVENTORYBYIDRESPONSE._serialized_end=898
  _GETUNITTYPEBYIDRESPONSE._serialized_start=900
  _GETUNITTYPEBYIDRESPONSE._serialized_end=965
  _GETPRODUCTINVENTORYBYUSERIDANDQUANTITYREQUEST._serialized_start=967
  _GETPRODUCTINVENTORYBYUSERIDANDQUANTITYREQUEST._serialized_end=1059
  _CHANGEPRODUCTINVENTORYCOUNTREQUEST._serialized_start=1061
  _CHANGEPRODUCTINVENTORYCOUNTREQUEST._serialized_end=1145
  _PRODUCTINVENTORYLISTRESPONSE._serialized_start=1147
  _PRODUCTINVENTORYLISTRESPONSE._serialized_end=1233
  _GETPRODUCTINVENTORYBYUSERIDREQUEST._serialized_start=1235
  _GETPRODUCTINVENTORYBYUSERIDREQUEST._serialized_end=1294
  _GETRETAILERPRODUCTLISTREQUEST._serialized_start=1296
  _GETRETAILERPRODUCTLISTREQUEST._serialized_end=1384
  _GETRETAILERPRODUCTLISTRESPONSE._serialized_start=1386
  _GETRETAILERPRODUCTLISTRESPONSE._serialized_end=1474
  _INVENTORYSERVICE._serialized_start=1477
  _INVENTORYSERVICE._serialized_end=2300
# @@protoc_insertion_point(module_scope)
