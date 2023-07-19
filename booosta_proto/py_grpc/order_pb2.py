# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: order.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0border.proto\x12\x05order\x1a\x1bgoogle/protobuf/empty.proto\"\x90\x02\n\x05Order\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x63ustomer_id\x18\x02 \x01(\t\x12\x14\n\x0cpayment_type\x18\x03 \x01(\t\x12\x16\n\x0epayment_option\x18\x04 \x01(\t\x12\x16\n\x0e\x61mount_payment\x18\x05 \x01(\x02\x12\x14\n\x0cshipping_fee\x18\x06 \x01(\x02\x12\x0f\n\x07\x62\x61lance\x18\x07 \x01(\x02\x12\x13\n\x0btotal_price\x18\x08 \x01(\x02\x12\x10\n\x08\x64iscount\x18\t \x01(\x02\x12\x13\n\x0bgrand_total\x18\n \x01(\x02\x12\x16\n\x0etransaction_id\x18\x0b \x01(\t\x12\x15\n\rcreated_by_id\x18\x0c \x01(\t\x12\x0e\n\x06status\x18\r \x01(\t\"\xc2\x01\n\tOrderItem\x12\x12\n\nproduct_id\x18\x01 \x01(\t\x12\x10\n\x08order_id\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\x03\x12\x1e\n\x16\x64iscount_selling_price\x18\x04 \x01(\x02\x12\x1a\n\x12product_cost_price\x18\x05 \x01(\x02\x12\x15\n\rselling_price\x18\x06 \x01(\x02\x12\x13\n\x0btotal_price\x18\x07 \x01(\x02\x12\x15\n\rcreated_by_id\x18\x08 \x01(\t\"\x9b\x01\n\x04\x43\x61rt\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nproduct_id\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\x03\x12\x15\n\rselling_price\x18\x04 \x01(\x02\x12\x1e\n\x16\x64iscount_selling_price\x18\x05 \x01(\x02\x12\x13\n\x0btotal_price\x18\x06 \x01(\x02\x12\x15\n\rcreated_by_id\x18\x07 \x01(\t\"!\n\x13GetOrderByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"Y\n*GetOrderByCreatedByIdAndPaymentTypeRequest\x12\x15\n\rcreated_by_id\x18\x01 \x01(\t\x12\x14\n\x0cpayment_type\x18\x02 \x01(\t\"%\n\x17GetOrderItemByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"3\n\x14GetOrderByIdResponse\x12\x1b\n\x05order\x18\x01 \x01(\x0b\x32\x0c.order.Order\"J\n+GetOrderByCreatedByIdAndPaymentTypeResponse\x12\x1b\n\x05order\x18\x01 \x03(\x0b\x32\x0c.order.Order\"@\n\x18GetOrderItemByIdResponse\x12$\n\norder_item\x18\x01 \x01(\x0b\x32\x10.order.OrderItem\"5\n\x1fGetOrderItemsByProductIdRequest\x12\x12\n\nproduct_id\x18\x01 \x01(\t\"1\n\x1dGetOrderItemsByOrderIdRequest\x12\x10\n\x08order_id\x18\x01 \x01(\t\"Z\n-GetOrderItemsByProductIdAndCreatedByIdRequest\x12\x15\n\rcreated_by_id\x18\x01 \x01(\t\x12\x12\n\nproduct_id\x18\x02 \x01(\t\":\n!GetOrderItemsByCreatedByIdRequest\x12\x15\n\rcreated_by_id\x18\x01 \x01(\t\">\n\x16OrderItemsListResponse\x12$\n\norder_item\x18\x01 \x03(\x0b\x32\x10.order.OrderItem\"f\n\x08\x43ustomer\x12\x15\n\rcustomer_name\x18\x01 \x01(\t\x12\x16\n\x0e\x63ustomer_phone\x18\x02 \x01(\t\x12\x16\n\x0e\x63ustomer_email\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\"$\n\x16GetCustomerByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"<\n\x17GetCustomerByIdResponse\x12!\n\x08\x63ustomer\x18\x01 \x01(\x0b\x32\x0f.order.Customer\"9\n\x14\x43ustomerListResponse\x12!\n\x08\x63ustomer\x18\x01 \x03(\x0b\x32\x0f.order.Customer\"<\n&GetOrderItemQuantityByProductIdRequest\x12\x12\n\nproduct_id\x18\x01 \x01(\t\";\n\'GetOrderItemQuantityByProductIdResponse\x12\x10\n\x08quantity\x18\x01 \x01(\x03\"7\n\x1eGetCustomersByCreatedByRequest\x12\x15\n\rcreated_by_id\x18\x01 \x01(\t\"E\n\x1fGetCustomersByCreatedByResponse\x12\"\n\tcustomers\x18\x01 \x03(\x0b\x32\x0f.order.Customer\"5\n\x16UpdateOrderByIdRequest\x12\x1b\n\x05order\x18\x01 \x01(\x0b\x32\x0c.order.Order\"6\n\x17UpdateOrderByIdResponse\x12\x1b\n\x05order\x18\x01 \x01(\x0b\x32\x0c.order.Order\"=\n\'RemoveProductFromCartByProductIdRequest\x12\x12\n\nproduct_id\x18\x01 \x01(\t\"<\n(RemoveProductFromCartByProductIdResponse\x12\x10\n\x08response\x18\x01 \x01(\t\"1\n\x1aGetCustomerDebtByIdRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\"+\n\x1bGetCustomerDebtByIdResponse\x12\x0c\n\x04\x64\x65\x62t\x18\x01 \x01(\x02\"I\n\x1dUpdateCustomerDebtByIdRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12\x13\n\x0b\x61mount_paid\x18\x02 \x01(\x02\"C\n\x1eUpdateCustomerDebtByIdResponse\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65\x62t\x18\x02 \x01(\x02\"/\n\x19GetCartByProductIdRequest\x12\x12\n\nproduct_id\x18\x01 \x01(\t\"7\n\x1aGetCartByProductIdResponse\x12\x19\n\x04\x63\x61rt\x18\x01 \x01(\x0b\x32\x0b.order.Cart2\xcf\r\n\x0cOrderService\x12I\n\x0cGetOrderById\x12\x1a.order.GetOrderByIdRequest\x1a\x1b.order.GetOrderByIdResponse\"\x00\x12U\n\x10GetOrderItemById\x12\x1e.order.GetOrderItemByIdRequest\x1a\x1f.order.GetOrderItemByIdResponse\"\x00\x12\x63\n\x18GetOrderItemsByProductId\x12&.order.GetOrderItemsByProductIdRequest\x1a\x1d.order.OrderItemsListResponse\"\x00\x12R\n\x0fGetCustomerById\x12\x1d.order.GetCustomerByIdRequest\x1a\x1e.order.GetCustomerByIdResponse\"\x00\x12\x82\x01\n\x1fGetOrderItemQuantityByProductId\x12-.order.GetOrderItemQuantityByProductIdRequest\x1a..order.GetOrderItemQuantityByProductIdResponse\"\x00\x12g\n\x1aGetOrderItemsByCreatedById\x12(.order.GetOrderItemsByCreatedByIdRequest\x1a\x1d.order.OrderItemsListResponse\"\x00\x12\x8e\x01\n#GetOrderByCreatedByIdAndPaymentType\x12\x31.order.GetOrderByCreatedByIdAndPaymentTypeRequest\x1a\x32.order.GetOrderByCreatedByIdAndPaymentTypeResponse\"\x00\x12\x7f\n&GetOrderItemsByProductIdAndCreatedById\x12\x34.order.GetOrderItemsByProductIdAndCreatedByIdRequest\x1a\x1d.order.OrderItemsListResponse\"\x00\x12K\n\x10GetAllOrderItems\x12\x16.google.protobuf.Empty\x1a\x1d.order.OrderItemsListResponse\"\x00\x12H\n\x0fGetAllCustomers\x12\x16.google.protobuf.Empty\x1a\x1b.order.CustomerListResponse\"\x00\x12j\n\x17GetCustomersByCreatedBy\x12%.order.GetCustomersByCreatedByRequest\x1a&.order.GetCustomersByCreatedByResponse\"\x00\x12_\n\x16GetOrderItemsByOrderId\x12$.order.GetOrderItemsByOrderIdRequest\x1a\x1d.order.OrderItemsListResponse\"\x00\x12R\n\x0fUpdateOrderById\x12\x1d.order.UpdateOrderByIdRequest\x1a\x1e.order.UpdateOrderByIdResponse\"\x00\x12\x85\x01\n RemoveProductFromCartByProductId\x12..order.RemoveProductFromCartByProductIdRequest\x1a/.order.RemoveProductFromCartByProductIdResponse\"\x00\x12^\n\x13GetCustomerDebtById\x12!.order.GetCustomerDebtByIdRequest\x1a\".order.GetCustomerDebtByIdResponse\"\x00\x12g\n\x16UpdateCustomerDebtById\x12$.order.UpdateCustomerDebtByIdRequest\x1a%.order.UpdateCustomerDebtByIdResponse\"\x00\x12[\n\x12GetCartByProductId\x12 .order.GetCartByProductIdRequest\x1a!.order.GetCartByProductIdResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'order_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_ORDER']._serialized_start=52
  _globals['_ORDER']._serialized_end=324
  _globals['_ORDERITEM']._serialized_start=327
  _globals['_ORDERITEM']._serialized_end=521
  _globals['_CART']._serialized_start=524
  _globals['_CART']._serialized_end=679
  _globals['_GETORDERBYIDREQUEST']._serialized_start=681
  _globals['_GETORDERBYIDREQUEST']._serialized_end=714
  _globals['_GETORDERBYCREATEDBYIDANDPAYMENTTYPEREQUEST']._serialized_start=716
  _globals['_GETORDERBYCREATEDBYIDANDPAYMENTTYPEREQUEST']._serialized_end=805
  _globals['_GETORDERITEMBYIDREQUEST']._serialized_start=807
  _globals['_GETORDERITEMBYIDREQUEST']._serialized_end=844
  _globals['_GETORDERBYIDRESPONSE']._serialized_start=846
  _globals['_GETORDERBYIDRESPONSE']._serialized_end=897
  _globals['_GETORDERBYCREATEDBYIDANDPAYMENTTYPERESPONSE']._serialized_start=899
  _globals['_GETORDERBYCREATEDBYIDANDPAYMENTTYPERESPONSE']._serialized_end=973
  _globals['_GETORDERITEMBYIDRESPONSE']._serialized_start=975
  _globals['_GETORDERITEMBYIDRESPONSE']._serialized_end=1039
  _globals['_GETORDERITEMSBYPRODUCTIDREQUEST']._serialized_start=1041
  _globals['_GETORDERITEMSBYPRODUCTIDREQUEST']._serialized_end=1094
  _globals['_GETORDERITEMSBYORDERIDREQUEST']._serialized_start=1096
  _globals['_GETORDERITEMSBYORDERIDREQUEST']._serialized_end=1145
  _globals['_GETORDERITEMSBYPRODUCTIDANDCREATEDBYIDREQUEST']._serialized_start=1147
  _globals['_GETORDERITEMSBYPRODUCTIDANDCREATEDBYIDREQUEST']._serialized_end=1237
  _globals['_GETORDERITEMSBYCREATEDBYIDREQUEST']._serialized_start=1239
  _globals['_GETORDERITEMSBYCREATEDBYIDREQUEST']._serialized_end=1297
  _globals['_ORDERITEMSLISTRESPONSE']._serialized_start=1299
  _globals['_ORDERITEMSLISTRESPONSE']._serialized_end=1361
  _globals['_CUSTOMER']._serialized_start=1363
  _globals['_CUSTOMER']._serialized_end=1465
  _globals['_GETCUSTOMERBYIDREQUEST']._serialized_start=1467
  _globals['_GETCUSTOMERBYIDREQUEST']._serialized_end=1503
  _globals['_GETCUSTOMERBYIDRESPONSE']._serialized_start=1505
  _globals['_GETCUSTOMERBYIDRESPONSE']._serialized_end=1565
  _globals['_CUSTOMERLISTRESPONSE']._serialized_start=1567
  _globals['_CUSTOMERLISTRESPONSE']._serialized_end=1624
  _globals['_GETORDERITEMQUANTITYBYPRODUCTIDREQUEST']._serialized_start=1626
  _globals['_GETORDERITEMQUANTITYBYPRODUCTIDREQUEST']._serialized_end=1686
  _globals['_GETORDERITEMQUANTITYBYPRODUCTIDRESPONSE']._serialized_start=1688
  _globals['_GETORDERITEMQUANTITYBYPRODUCTIDRESPONSE']._serialized_end=1747
  _globals['_GETCUSTOMERSBYCREATEDBYREQUEST']._serialized_start=1749
  _globals['_GETCUSTOMERSBYCREATEDBYREQUEST']._serialized_end=1804
  _globals['_GETCUSTOMERSBYCREATEDBYRESPONSE']._serialized_start=1806
  _globals['_GETCUSTOMERSBYCREATEDBYRESPONSE']._serialized_end=1875
  _globals['_UPDATEORDERBYIDREQUEST']._serialized_start=1877
  _globals['_UPDATEORDERBYIDREQUEST']._serialized_end=1930
  _globals['_UPDATEORDERBYIDRESPONSE']._serialized_start=1932
  _globals['_UPDATEORDERBYIDRESPONSE']._serialized_end=1986
  _globals['_REMOVEPRODUCTFROMCARTBYPRODUCTIDREQUEST']._serialized_start=1988
  _globals['_REMOVEPRODUCTFROMCARTBYPRODUCTIDREQUEST']._serialized_end=2049
  _globals['_REMOVEPRODUCTFROMCARTBYPRODUCTIDRESPONSE']._serialized_start=2051
  _globals['_REMOVEPRODUCTFROMCARTBYPRODUCTIDRESPONSE']._serialized_end=2111
  _globals['_GETCUSTOMERDEBTBYIDREQUEST']._serialized_start=2113
  _globals['_GETCUSTOMERDEBTBYIDREQUEST']._serialized_end=2162
  _globals['_GETCUSTOMERDEBTBYIDRESPONSE']._serialized_start=2164
  _globals['_GETCUSTOMERDEBTBYIDRESPONSE']._serialized_end=2207
  _globals['_UPDATECUSTOMERDEBTBYIDREQUEST']._serialized_start=2209
  _globals['_UPDATECUSTOMERDEBTBYIDREQUEST']._serialized_end=2282
  _globals['_UPDATECUSTOMERDEBTBYIDRESPONSE']._serialized_start=2284
  _globals['_UPDATECUSTOMERDEBTBYIDRESPONSE']._serialized_end=2351
  _globals['_GETCARTBYPRODUCTIDREQUEST']._serialized_start=2353
  _globals['_GETCARTBYPRODUCTIDREQUEST']._serialized_end=2400
  _globals['_GETCARTBYPRODUCTIDRESPONSE']._serialized_start=2402
  _globals['_GETCARTBYPRODUCTIDRESPONSE']._serialized_end=2457
  _globals['_ORDERSERVICE']._serialized_start=2460
  _globals['_ORDERSERVICE']._serialized_end=4203
# @@protoc_insertion_point(module_scope)
