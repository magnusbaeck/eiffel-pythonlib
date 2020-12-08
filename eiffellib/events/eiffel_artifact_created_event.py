# Copyright 2019 Axis Communications AB.
#
# For a full list of individual contributors, please see the commit history.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""EiffelArtifactCreatedEvent.

https://github.com/eiffel-community/eiffel/blob/master/eiffel-vocabulary/EiffelArtifactCreatedEvent.md
"""
import time
import uuid
from enum import Enum
from typing import List
from typing import Optional

import pydantic


class EiffelMetaSource(pydantic.BaseModel):
    domainId: Optional[str]
    host: Optional[str]
    name: Optional[str]
    serializer: Optional[str]
    uri: Optional[str]


class EiffelMeta(pydantic.BaseModel):
    id: uuid.UUID
    type: str
    version: str
    time: int
    tags: Optional[List[str]]
    source: Optional[EiffelMetaSource]


class EiffelArtifactCreatedFileInfo(pydantic.BaseModel):
    name: str
    tags: Optional[List[str]]


class EiffelArtifactRequiresImpl(str, Enum):
    NONE = "NONE"
    ANY = "ANY"
    EXACTLY_ONE = "EXACTLY_ONE"
    AT_LEAST_ONE = "AT_LEAST_ONE"


class EiffelArtifactCreatedData(pydantic.BaseModel):
    identity: str
    fileInformation: Optional[List[EiffelArtifactCreatedFileInfo]]
    buildCommand: Optional[str]
    requiresImplementation: Optional[EiffelArtifactRequiresImpl]
    implements: Optional[List[str]]
    dependsOn: Optional[List[str]]
    name: Optional[str]


class EiffelLink(pydantic.BaseModel):
    type: str
    target: uuid.UUID


class EiffelArtifactCreatedEvent(pydantic.BaseModel):
    meta: EiffelMeta = None
    data: EiffelArtifactCreatedData
    links: List[EiffelLink] = []

    @pydantic.validator("meta", pre=True, always=True)
    def default_meta(cls, v):
        return v or EiffelMeta(
            id=uuid.uuid4(),
            type="EiffelArtifactCreatedEvent",
            version="3.0.0",
            time=time.time() * 1000,
        )
