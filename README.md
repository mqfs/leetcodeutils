# leetcodeutils
## Introduction
Some useful utilities for coding with Leetcode in PyCharm.  
Support features:  
1. Directly debugging and get output in PyCharm with Leetcode problems by using the most simple codes. (tips: implemented by reflection and support the most problems in Leetcode)  
2. Coming soon.  
## Usage
1. Install the latest version by pip under python3: `pip install leetcodeutils`  
2. In your `main.py`, 
   1. Instantiate a case wrapper of `CaseWrapper` with initial arguments of directly test case in Leetcode problem like `"babad"`, just copy-paste what case you saw in Leetcode problem.  
   2. Instantiate a case executor of `CaseExecutor` with initial arguments of target class like `Solution`, target method string like `"addTwoNumbers"` for Leetcode No.2 problem, former case wrapper.  
   3. Invoke the method `execute` of case executor instance, **the Leetcode's style output will be returned**.

For more detailed usage, just see [SimpleExample.py](https://github.com/mqfs/leetcodeutils/blob/master/leetcodeutils/SimpleExample.py), [TreeNodeExample.py](https://github.com/mqfs/leetcodeutils/blob/master/leetcodeutils/TreeNodeExample.py), [ListNodeExample.py](https://github.com/mqfs/leetcodeutils/blob/master/leetcodeutils/ListNodeExample.py), [ComplexExample.py](https://github.com/mqfs/leetcodeutils/blob/master/leetcodeutils/ComplexExample.py)  
## License
leetcodeutils is MIT licensed, as found in the [LICENSE](https://github.com/mqfs/leetcodeutils/blob/master/LICENSE.txt) file.
## Other
Maintained by Gancheng Yuan  
Having fun in Leetcode. ^ v ^