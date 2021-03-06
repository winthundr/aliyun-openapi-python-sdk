# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest

class GrantDbToAccountRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'retailcloud', '2018-03-13', 'GrantDbToAccount','retailcloud')
		self.set_method('POST')

	def get_AccountName(self):
		return self.get_body_params().get('AccountName')

	def set_AccountName(self,AccountName):
		self.add_body_params('AccountName', AccountName)

	def get_DbName(self):
		return self.get_body_params().get('DbName')

	def set_DbName(self,DbName):
		self.add_body_params('DbName', DbName)

	def get_DbInstanceId(self):
		return self.get_body_params().get('DbInstanceId')

	def set_DbInstanceId(self,DbInstanceId):
		self.add_body_params('DbInstanceId', DbInstanceId)

	def get_AccountPrivilege(self):
		return self.get_body_params().get('AccountPrivilege')

	def set_AccountPrivilege(self,AccountPrivilege):
		self.add_body_params('AccountPrivilege', AccountPrivilege)