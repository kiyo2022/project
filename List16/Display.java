package List16;

/**
 * ディスプレイ
 */
public class Display {

	/********************************
	 * 画面へ出力するメッセージのガワ作り
	 * enumで定義している
	 ************************************************************************/
	protected enum DesplayMessage {                   /*↓機種依存による改行*/
		GameStart("*******チップ枚数とカード*******" + getLineSeparator() +
				"総計： %d ([10]：%d枚 [1]：%d枚)" + getLineSeparator() +
				"現在のカード： %s" + getLineSeparator() +
				"********************************"),
		GameSituation("**********Big or Small**********" + getLineSeparator() +
				"BET数：  %d " + getLineSeparator() +
				"あなたの選択： %s" + getLineSeparator() +
				"現在のカード： %s" + getLineSeparator() +
				"引いたカード： %s" + getLineSeparator() +
				"%s は %s より %s" + getLineSeparator() +
				"********************************"),
		GameWin("Win!!" + getLineSeparator() + "チップ%d枚を獲得しました " + getLineSeparator() + getLineSeparator()),
		GameLoss("Lose..." + getLineSeparator() + getLineSeparator()),
		GameResult("********現在のチップ枚数********" + getLineSeparator() +
				"総計：%d ([10]：%d枚 [1]：%d枚)" + getLineSeparator() +
				"********************************"),
		GameEnd("End"),
		BigSelect("Big"),
		SmallSelect("Small");

		public final String message;

		private DesplayMessage(String message) {
			this.message = message;
		}
		/*******************************************
		 * 変数formatで引数をいくらでも書けるようにしてあって
		 * そのメッセージと一緒に引数を返す様にしている
		 ********************************************/
		public String format(Object... args) {
			return String.format(message, args);
		}
	}

	/**
	 * 画面へ１行表示する
	 * @param string 表示する文字列
	 */
	public static void println(String string) {
		System.out.println(string);
	}

	/**
	 * 機種依存の改行コードを取得する
	 * @return 改行コード
	 */
	public static String getLineSeparator() {
		return System.getProperty("line.separator");
	}

	/**************************************************************
	 * ゲーム開始の時に実際に表示される文
	 * @param chips 手持ちのチップ
	 * @param firstCard  最初のカード
	 **************************************************************/
	public void viewGameStart(Chips chips, Card firstCard) {
		println(DesplayMessage.GameStart.format(
				chips.getTatal(),
				chips.getTenValue(),
				chips.getOneValue(),
				firstCard.toString()));
	}

	/*************************************************************************************************************
	 * プレイヤーがBigOrSmallを選択した後のゲーム状況を実際に表示させる文
	 * @param tableChip テーブル上のチップ
	 * @param bigOrSmall プレイヤーの選択
	 * @param firstCard 最初のカード
	 * @param secondCard 最初のカード
	 *******************************************************************************************************/
	public void viewGameSituation(long tableChip, boolean bigOrSmall, Card firstCard, Card secondCard) {
		/**********************************************************************************************************
		 * プレイヤーがBigかSmallのどちらを選んだかを返してselectに放り込む
		 *******************************************************************************************************/
		String select = (bigOrSmall) ? DesplayMessage.BigSelect.message : DesplayMessage.SmallSelect.message;
		/**********************************************************************************************************
		 * firstCardとsecondCardを見比べて大きければBig,小さければSmallをresultに放り込む
		 *******************************************************************************************************/
		String result = (firstCard.isBigOrSmall(secondCard)) ? DesplayMessage.BigSelect.message : DesplayMessage.SmallSelect.message;
		println(DesplayMessage.GameSituation.format(
				tableChip,
				select,
				firstCard.toString(),
				secondCard.toString(),
				secondCard.toString(),
				firstCard.toString(),
				result));
	}

	/*****************************************************
	 * ゲーム勝利したときに表示させる文
	 * @param tableChip テーブル上のチップ
	 **********************************************************/
	public void viewWin(long tableChip) {
		println(DesplayMessage.GameWin.format(tableChip));
	}

	/********************************************************
	 * ゲーム敗退した時に表示させる文
	 *******************************************************/
	public void viewLoss() {
		println(DesplayMessage.GameLoss.message);
	}

	/***************************************************************************
	 * ゲーム結果を表示させる文
	 * @param chips 手持ちのチップ
	 ****************************************************************************/
	public void viewGameResult(Chips chips) {
		println(DesplayMessage.GameResult.format(chips.getTatal(), chips.getTenValue(), chips.getOneValue()));
	}

	/******************************************************************************
	 * ゲーム終了
	 *******************************************************************************/
	public void viewEnd() {
		println(DesplayMessage.GameEnd.message);
	}

}