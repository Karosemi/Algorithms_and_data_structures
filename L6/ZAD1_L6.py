class TreeNode:
    def __init__(self,key,val,left=None,right=None, parent=None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.left_child

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self
    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                    self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                    self.right_child.parent = self.parent


    def find_successor(self):
        succ = None
        if self.has_right_child():
            succ = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self
        return succ


    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
            self.size = self.size + 1

    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)
        elif key == current_node.key:
            current_node.payload = val
            # if not current_node.has_any_children():
            #     print('ccc', not current_node.has_any_children())
            #     if current_node.is_left_child():
            #         current_node.left_child = TreeNode(key - 1, val, parent=current_node)
            #         print(f"Choosen key is in usage. Selected another key with value {key-1}")
            #         self.size += 1
            #         return key - 1
            #
            #     elif current_node.is_right_child():
            #         current_node.right_child = TreeNode(key + 1, val, parent=current_node)
            #         print(f"Choosen key is in usage. Selected another key with value {key+1}")
            #         self.size += 1
            #         return key + 1
            # else:
            #     print('cddcc', not current_node.has_any_children())
            #     if current_node.is_left_child():
            #         temp = current_node
            #         key += 1
            #         right_child = current_node.right_child
            #
            #         left_child = current_node.left_child
            #         current_node.left_child = TreeNode(key, val, parent=current_node)
            #         self.__put_children(current_node, right_child, left_child)
            #         # current_node.left_child = temp
            #
            #
            #         print(f"Choosen key is in usage. Selected another key withss vmalue {key}")
            #         self.size += 1
            #         return key
            #     elif current_node.is_right_child():
            #         temp = current_node
            #         key -= 1
            #         right_child = current_node.right_child
            #         left_child = current_node.left_child
            #         current_node.right_child = TreeNode(key, val, parent=current_node)
            #         current_node = self.__put_children__(right_child, current_node)
            #         current_node = self.__put_children__(left_child, current_node)
            #         # self.__put_children(current_node, right_child, left_child)
            #         print(f"Choosen key is in usage. Selected another key withss value {key}")
            #         self.size += 1
            #         return key
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)

    def __put_children__(self, subtree,  current):
        if subtree.has_any_children():
            right = subtree.right_child
            left = subtree.left_child
            left_val = left.payload
            left_key = left.key
            right_key = right.key
            right_val = right.payload
            if left:
                self._put(left_key, left_val, current)
                self.__put_children(left, current)
            if right:
                self._put(right_key, right_val, current)
                self.__put_children(right, current)
        return current


    def __put_children(self, current, first_child = None, second_child = None):
        if not current.has_any_children():
            if first_child is not None:
                if first_child.key < current.key():
                    current.left_child = first_child
                elif first_child.key > current.key():
                    current.right_child = first_child
            if second_child is not None:
                if second_child.key < current.key():
                    current.left_child = second_child
                elif second_child.key > current.key():
                    current.right_child = second_child
        else:
            if first_child is not None:
                if first_child.key < current.key:
                    self.__put_children(current.left_child, current.left_child.right_child, current.left_child.left_child)
                if first_child.key > current.key:
                    self.__put_children(current.right_child, current.right_child.right_child,
                                        current.right_child.left_child)

            if second_child is not None:
                if second_child.key > current.key:
                    self.__put_children(current.right_child, first_child, second_child)

    def __setitem__(self, k, v): #overloading of [] operator
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def __getitem__(self, key): #overloading of [] operator
        return self.get(key)

    def __contains__(self, key): # overloading of in operator
        if self._get(key,self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size = self.size-1
            else:
                raise KeyError('Error, key not in tree.')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key): #overloading of del operator
        self.delete(key)

    def remove(self, current_node):
        if current_node.is_leaf(): #leaf
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_both_children(): #interior
            succ = current_node.find_successor()
            succ.splice_out()
            current_node.key = succ.key
            current_node.payload = succ.payload
        else: # this node has one child
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.replace_node_data(current_node.left_child.key,
                                                   current_node.left_child.payload,
                                                   current_node.left_child.left_child,
                                                   current_node.left_child.right_child)
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_node_data(current_node.right_child.key,
                                                   current_node.right_child.payload,
                                                   current_node.right_child.left_child,
                                                   current_node.right_child.right_child)


class BST(BinarySearchTree):

    def __init__(self):
        super().__init__()

    def put(self, key, value):
        prev_key = key
        if self.root:
            if self.root.key == key:
                print("Selected key is a root key, choose another key.")
                return
        while self.get(key) is not None:
            if key < self.root.key:
                key -= 1
            elif key > self.root.key:
                key += 1
        if prev_key != key:
            print(f"Choosen key is in usage. Selected another key with value {key}")

        super().put(key=key, val=value)

    def __len__(self):
        return super().__len__()

    def __iter__(self):
        return super().__iter__()

    def get(self, key):
        return super().get(key)

    def __setitem__(self, k, v): #overloading of [] operator
        self.put(k, v)

    def __getitem__(self, key): #overloading of [] operator
        return self.get(key)

    def __contains__(self, key): # overloading of in operator
        if super()._get(key, self.root):
            return True
        else:
            return False

    def delete(self,key):
        super().delete(key)

    def __delitem__(self,key): #overloading of del operator
        self.delete(key)

    def splice_out(self):
        super().splice_out()

    def find_successor(self):
        return super().find_successor()

    def find_min(self):
        return super().find_min()

    def remove(self, current_node):
        super().remove(current_node)


if __name__ == '__main__':
    mytree = BinarySearchTree()
    mytree[13] = "red"
    mytree[4] = "blue"
    mytree[61] = "yellow"
    mytree[14] = "at"
    mytree[65] = "cos"
    mytree.put(61, "nowe cos")
    print(mytree[61])
    print(mytree[3])
    print(mytree[4])
    print(mytree[14])
    print(mytree[13])
    print(mytree[61])
    print(mytree[60])
    # mytree.splice_out()