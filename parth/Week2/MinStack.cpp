class MinStack {
private:
    vector<int> stack;
    int minIndex;
public:
    MinStack() {
        minIndex = -1;
    }
    
    void push(int val) {
        if(minIndex == -1 || val < stack[minIndex])
        {
            stack.push_back(minIndex);
            minIndex = stack.size();
        }
        stack.push_back(val);
    }
    
    void pop() {
        int currentBackVal = stack.back();
        stack.pop_back();
        if(minIndex == stack.size())
        {
            minIndex = stack.back();
            stack.pop_back();
        }
    }
    
    int top() {
        return stack.back();
    }
    
    int getMin() {
        return stack[minIndex];
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */