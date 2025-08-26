`2025-08-27`

## 問題: 2番目に大きい数を探せ

整数の配列 `nums` が与えられます。
**2番目に大きい数** を返してください。

* 配列の長さは **2以上** とする。
* 同じ値が複数あっても「順位」として数える。
  例: `[5, 5, 4]` → 2番目に大きいのは `4`。

---

### 入力例 1

```
nums = [2, 7, 3, 1, 7]
```

出力:

```
3
```

（最大は7、2番目は3）

### 入力例 2

```
nums = [10, 9]
```

出力:

```
9
```

---

### 学びポイント

* ソートして取り出すのは簡単だが **O(n log n)**。
* 実は **1パス O(n)** で「最大値」「2番目の最大値」を同時に管理できる。
* 「状態を2つ持って更新する」パターンは **選択型DPやスライディングウィンドウ**でもよく使う。

> こんなんでどうですか？
> 
> ```python
> def test_2nd_largest_2():
>     nums = [2, 7, 3, 1, 7]
>     v_1st, v_2nd = 0, 0
>     for num in nums:
>         prev_1st = v_1st
>         if v_2nd < num and v_1st < num:
>             v_1st = num
>             v_2nd = max(v_2nd, prev_1st)
>         if v_2nd < num and num < v_1st:
>             v_2nd = num
>     assert v_2nd == 3
> ```

良いですね！👏
「1番目と2番目を更新しながら走査する」基本方針はしっかりできています。
ただ少し整理すると **よりシンプルかつバグ耐性が高い実装** になります。

---

### 今のコードの懸念点

1. `v_1st, v_2nd = 0, 0` の初期化

   * 配列に負の数が含まれると壊れてしまう（例: `[-5, -2, -3]`）。
   * → **`float('-inf')` で初期化**すると安全。

2. 条件分岐がやや複雑

   * `if v_2nd < num and v_1st < num:` と `if v_2nd < num and num < v_1st:` の2本立て。
   * 実は \*\*「最大更新」と「2番目更新」で分ける」\*\*だけで済む。

---

### 改善版（1パス O(n)）

```python
def second_largest(nums: list[int]) -> int:
    v_1st = float('-inf')
    v_2nd = float('-inf')
    for num in nums:
        if num > v_1st:          # 最大更新
            v_1st, v_2nd = num, v_1st
        elif v_1st > num > v_2nd:  # 2番目更新
            v_2nd = num
    return v_2nd
```

---

### テスト

```python
assert second_largest([2, 7, 3, 1, 7]) == 3
assert second_largest([10, 9]) == 9
assert second_largest([-5, -2, -3]) == -3
assert second_largest([5, 5, 4]) == 4
```

---

👉 学びポイント

* **初期値に `-inf` を使うパターン**は競技プログラミングやDPでも頻出。
* 「状態を持って走査する」ことで **ソート不要で効率化**できる。
* 更新条件を分けすぎず、`if / elif` で整理するのがバグを減らすコツ。

---

次は同じ「2番目シリーズ」で
📌 **2番目に小さい数**
📌 **k番目に大きい数（一般化）**

のどちらに進めましょうか？

---

> k番目に大きい数で進めてみましょうか？

いいですね！🎯
「k番目に大きい数」は、典型的に **3種類のアプローチ** が学びになります。

---

## 問題: k番目に大きい数

整数配列 `nums` と整数 `k` が与えられます。
**k番目に大きい数** を返してください。

* 配列は空でない
* 1 ≤ k ≤ len(nums)

---

### 入力例 1

```
nums = [3, 2, 1, 5, 6, 4], k = 2
```

出力:

```
5
```

（2番目に大きい数は 5）

### 入力例 2

```
nums = [7, 10, 4, 3, 20, 15], k = 3
```

出力:

```
10
```

---

## アプローチ3種

### 1. **ソート（簡単だけど O(n log n)）**

```python
def kth_largest(nums: list[int], k: int) -> int:
    nums.sort(reverse=True)
    return nums[k-1]
```

---

### 2. **最小ヒープ（効率的 O(n log k)）**

Python の `heapq` を使うと「常に k 個だけ保持」ができる。

```python
import heapq

def kth_largest(nums: list[int], k: int) -> int:
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)  # 一番小さいのを捨てる
    return heap[0]
```

---

### 3. **クイックセレクト（平均 O(n)）**

クイックソートの仕組みを使って、
「k番目に大きい位置にある要素」を直接探す方法。
競技プログラミングやLeetCodeでよく出ます。

（ちょっと難しいので、希望があれば実装一緒にやりましょう）

---

👉 学びポイント

* **ソート**: 一番簡単、でも O(n log n)
* **ヒープ**: k が小さいとき効率的 O(n log k)
* **クイックセレクト**: 平均 O(n) で最速

---

ここから練習としては、

1. まずソート版を自分で実装
2. そのあとヒープ版に挑戦

という流れがちょうどいいと思います。

どちらからやってみますか？

---

> 見ずに行ったら 1に落ち着きましたね。
> ```python
> def nth_largest(nums: list[int], k: int) -> int:
>     unique_nums = list(set(nums))
>     sorted_unique_nums = sorted(unique_nums)
>     return sorted_unique_nums[-k]
> ```

