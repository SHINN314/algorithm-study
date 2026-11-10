import pprint
import numpy as np

def calculate_convex_hull(p):
    """凸包を計算するプログラム．

    Parameters
    ----------
    p: 
        2次元平面上の点を集めたリスト．
    
    Returns
    ----------
    ch: 
        凸包を表現するのに必要な最小の点集合．
    """
    # 定数の宣言
    p_num = p.shape[0]
    
    # x座標の値順にpの要素をソート
    p = sorted(p, key=lambda x: x[0])

    # 上側凸包の計算
    lu = np.array([p[0], p[1]])

    for i in range(2, p_num):
        lu = np.vstack([lu, p[i]])

        while (lu.shape[0] >= 3):
            # luの末尾3つの点を取得
            p_l3 = lu[-3, :]
            p_l2 = lu[-2, :]
            p_l1 = lu[-1, :]

            signed_area = (p_l3[0] - p_l2[0]) * (p_l2[1] - p_l1[1]) - (p_l3[1] - p_l2[1]) * (p_l2[0] - p_l1[0])

            # 右回りならwhileを抜ける
            if signed_area < 0:
                break

            lu = np.delete(lu, -2, axis=0)

    # 下側凸包の計算
    ll = np.array([p[-1], p[-2]])

    for i in reversed(range(p_num - 2)):
        ll = np.vstack([ll, p[i]])

        while (ll.shape[0] >= 3):
            # llの末尾3点を取得
            p_l3 = lu[-3, :]
            p_l2 = lu[-2, :]
            p_l1 = lu[-1, :]

            signed_area = (p_l3[0] - p_l2[0]) * (p_l2[1] - p_l1[1]) - (p_l3[1] - p_l2[1]) * (p_l2[0] - p_l1[0])

            # 右回りならwhileを抜ける．
            if signed_area < 0:
                break

            lu = np.delete(ll, -2, axis=0)

    # 端点における重複を削除
    lu = np.delete(lu, -1, axis=0) # 右端の点を削除
    ll = np.delete(ll, -1, axis=0) # 左端の点を削除

    ch = np.concatenate([lu, ll], axis=0)

    return ch

if __name__=="__main__":
    p = np.array([[1, 2], [-1, 0], [0, 10], [-4, 9]])
    ch = calculate_convex_hull(p)
    pprint.pprint(ch, width=20)