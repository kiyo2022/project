package List16;

import java.util.ArrayList;
import java.util.Collections;

/**********************************************
 * トランプでArrayListの<Card>を継承している
 **********************************************/

public class Trump extends ArrayList<Card>{
	/*******************************************
	 * シリアライズバージョンID
	 * これは警告避け
	 ********************************************/

	private static final long serialVersionUID = 1L;


	/*************************************************
	 * コンストラクタ
	 * 最初にArrayList<card>の中身を全て削除する
	 * Cardクラスで作ったリスト1~13をそれぞれのマーク毎に
	 * 全てArrayList<card>にレベルが弱いマークから格納していってる
	 *
	 *************************************************/

	public Trump() {
		/*******************************************************
		 * superでArrayList<card>を最初に引っ張り出してきている
		 ******************************************************/
		super();
		// 初期化する
		this.clear();
		// クラブ
		this.addAll( Card.getNewInstance(CardMark.Clubs));
		// ダイヤ
		this.addAll( Card.getNewInstance(CardMark.Diamond));
		// ハート
		this.addAll( Card.getNewInstance(CardMark.Heart));
		// スペード
		this.addAll( Card.getNewInstance(CardMark.Spade));
	}
	/*******************************************************
	 * ArrayList<card>に入ったTrumpをシャッフルする
	 *
	 ******************************************************/
	public void shuffle() {
		Collections.shuffle(this);
	}
	/*********************************************************
	 *シャッフルしたArrayList<card>の一番目をresultに放り込んで
	 *returnで返している
	 *
	 * @return カード
	 *******************************************************/
	public Card getCard() {
		Card result = this.remove(0);
		this.add(result);
		return result;
	}
	/****************************************************
	 * 上の処理のカードcを引数とした場合のメソッド
	 *
	 * トランプからカードを取り出す
	 * 同一のカードならば別のカードにする
	 * @param c 比較するカード
	 * @return カード
	 ****************************************************/
	public Card getCard(Card c) {
		// カードを取り出す
		Card result = getCard();
		// 同じカードの場合は次を取り出す
		if (result.equals(c) ) {
			result = getCard();
		}
		return result;
	}
}