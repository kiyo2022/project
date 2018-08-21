package List16;

/**
 * BigOrSmall メインクラス
 */
public class BigOrSmall {

	/*********************************************
	 * 開始時のチップ総数を100枚に
	 * LはTrumpクラスのserialVersionUID表記に従う
	 *********************************************/

	private static final long StartChips = 100L;

	public static void main(String[] args) {
		// キーボードの生成
		Keyboard key = new Keyboard();
		// ディスプレイの生成
		Display display = new Display();
		// トランプの生成
		Trump trump = new Trump();
		// チップの生成
		Chips chips = new Chips(StartChips);
		// ゲーム開始する
		do {
			// Trumpクラスにあるシャッフルを使う
			trump.shuffle();
			// TrumpクラスにあるgetCardで最初のカードをひく
			Card firstCard = trump.getCard();
			// Displayクラスにあるゲーム開始の表示
			display.viewGameStart(chips, firstCard);
			/*******************************************************************************
			 * ベット数を入力して、それを手持ちのチップから引いてテーブル上のチップ数とする
			 * betChipsはChipsクラスから手持ちから掛け金引く処理
			 * betValueは掛け金を入力して返す処理
			 * ***************************************************************************/
			long tableChip = chips.betChips(key.betValue(chips));
			while (true) {
				// KeyboardクラスからBigOrSmallの選択を表示させる
				boolean bigOrSmall = key.isBigOrSmall(firstCard);
				// 次のカードをひく
				Card secondCard = trump.getCard(firstCard);
				// Displayクラスからゲームの状況を表示する
				display.viewGameSituation(tableChip, bigOrSmall, firstCard, secondCard);
				/*******************************************************************************
				 * 勝敗の決定
				 * 2枚目のカードから1枚目のカードを引いて
				 * マイナスならsmallプラスならbigをbigOrSmallに入れてる
				 * ***************************************************************************/
				if (bigOrSmall == firstCard.isBigOrSmall(secondCard)) {
					// 勝利したときの報酬を得る
					tableChip = chips.getReward(tableChip);
					// 勝利の表示
					display.viewWin(tableChip);
					// そのままゲームを続けるか選択する
					if (key.isNextBet(tableChip)) {
						// 引いたカードを最初のカードにする
						firstCard = secondCard;
						// そのままゲームを続ける
						continue;
					}
					// チップを精算する
					chips.payOff(tableChip);
				} else {
					// 敗退の表示
					display.viewLoss();
				}
				// 次のゲームへ
				break;
			}
			// チップ枚数を表示する
			display.viewGameResult(chips);
			// ゲームの終了判定
		} while (key.isGameEnd(chips));
		// 終了の表示
		display.viewEnd();
		// キーボードを閉じる
		key.close();
	}
}