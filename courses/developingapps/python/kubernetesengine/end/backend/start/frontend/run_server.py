# Copyright 2017 Google Inc.
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

from quiz import app

# TODO: Add the following statement to import and start
# Stackdriver debug-agent
# The start(...) method takes an 'options' object that you
# can use to configure the Stackdriver Debugger agent.
# You will need to pass through an object with an
# allowExpressions Boolean property set to true.

# END TODO

app.run(debug=True, port=8080)
