class BSTNode:
    def __init__(self, place_id, name, desc):
        self.place_id = place_id
        self.name = name
        self.desc = desc
        self.left = None
        self.right = None


class CampusBST:
    def __init__(self):
        self.root = None

    def insert(self, place_id, name, desc):
        new_node = BSTNode(place_id, name, desc)
        if self.root is None:
            self.root = new_node
            return
        cur = self.root
        while True:
            if place_id < cur.place_id:
                if cur.left is None:
                    cur.left = new_node
                    break
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = new_node
                    break
                cur = cur.right

    def search(self, key):
        cur = self.root
        while cur:
            if key == cur.place_id:
                return cur
            elif key < cur.place_id:
                cur = cur.left
            else:
                cur = cur.right
        return None

    def delete(self, key):
        parent = None
        cur = self.root
        # 先找到要删除的节点和其父节点
        while cur and cur.place_id != key:
            parent = cur
            if key < cur.place_id:
                cur = cur.left
            else:
                cur = cur.right
        if cur is None:
            return False

        # 情况1：左右都为空
        if cur.left is None and cur.right is None:
            if parent is None:
                self.root = None
            elif parent.left == cur:
                parent.left = None
            else:
                parent.right = None

        # 情况2：只有右孩子
        elif cur.left is None:
            if parent is None:
                self.root = cur.right
            elif parent.left == cur:
                parent.left = cur.right
            else:
                parent.right = cur.right

        # 情况3：只有左孩子
        elif cur.right is None:
            if parent is None:
                self.root = cur.left
            elif parent.left == cur:
                parent.left = cur.left
            else:
                parent.right = cur.left

        # 情况4：左右都有孩子，找后继节点（右子树最小值）
        else:
            succ_parent = cur
            succ = cur.right
            while succ.left:
                succ_parent = succ
                succ = succ.left
            cur.place_id = succ.place_id
            cur.name = succ.name
            cur.desc = succ.desc
            if succ_parent == cur:
                succ_parent.right = succ.right
            else:
                succ_parent.left = succ.right
        return True

    def inorder_traverse(self, node):
        if node:
            self.inorder_traverse(node.left)
            print(f"{node.place_id}: {node.name} - {node.desc}")
            self.inorder_traverse(node.right)


# 测试代码
if __name__ == "__main__":
    bst = CampusBST()
    bst.insert(1, "1#教学楼", "本科上课主楼")
    bst.insert(2, "2#食堂", "三餐就餐场所")
    bst.insert(5, "实训五号楼后侧小路", "非机动车近道")

    print("中序遍历：")
    bst.inorder_traverse(bst.root)

    res = bst.search(2)
    if res:
        print(f"\n查询结果：{res.place_id}:{res.name}-{res.desc}")

    bst.delete(2)
    print("\n删除2号节点后：")
    bst.inorder_traverse(bst.root)
