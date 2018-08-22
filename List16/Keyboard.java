package List16;

import java.util.Scanner;

/**
 * キーボード
 */
public class Keyboard {

	/***********************************
	 * 入力エラーメッセージ
	 * enumでそれぞれ定義している
	 **********************************/
	protected enum InputError {
		NumericCharacters("半角数字を入力してください。"),
		MinimumBet("BETするチップ数は、最低%d以上を入力してください。"),
		MaxmumBet("BETするチップ数は、最大%d以下で入力してください。"),
		NumericZeroOrOwn("半角数字の0あるいは1のみ入力してください。");

		public final String message;

		private InputError(String message) {
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

	/****************************************
	 * 入力プロンプト
	 * enumでそれぞれ定義している
	 *****************************************/
	protected enum Prompt {
		Betting("BETするチップの枚数を入力してください。（最低%d～最大%d）"),
		NextBetting("[獲得したチップ%d枚でBig or Smallを続けますか?]： 0:Yes 1:No"),
		BigOrSmall("[Big or Small]： 0:Big 1:Small"),
		GameEnd("[ゲームを続けますか?]： 0:Yes 1:NO"),
		NoChips("チップの総計が0になりましたので終了します。"),
		BigOrSmallSelecter("■ Big or Small選択" + Display.getLineSeparator() + "現在のカード： %s");
                                                         //↑機種依存に合わせた改行をしている
		public final String message;


		private Prompt(String message) {
			this.message = message;
		}

		/*******************************************
		 * 上記と同様
		 * 変数formatで引数をいくらでも書けるようにしてあって
		 * そのメッセージと一緒に引数を返す様にしている
		 ********************************************/
		public String format(Object... args) {
			return String.format(message, args);
		}

	}

	/********************************************
	 * スキャナーをscannerで定義してnullで初期化
	 *********************************************/
	private Scanner scanner = null;

	/*********************************************
	 * コンストラクタ
	 ************************************************/
	public Keyboard() {
		this.scanner = new Scanner(System.in);
	}

	/*******************************************************
	 * スキャナーを閉じる
	 ***************************************************/
	public void close() {
		this.scanner.close();
	}

	/*************************************************:
	 * ベット数の入力
	 * true引数できたらループさせ続ける
	 * @param chips
	 * @return
	 ********************************************************/
	public long betValue(Chips chips) {
		long result = 0;
		while (true) {
			/*******************************************************
			 * trueであれば 入力プロンプトのBettingからChipsクラスの
			 * 掛け金最小値、最大値を引っ張って表示している
			 ***************************************************/
			Display.println(Prompt.Betting.format(chips.getMinBetValue(), chips.getMaxBetValue()));
			/*******************************************************
			 * 次の行でin変数に文字入力
			 ***************************************************/
			String in = scanner.nextLine();
			/*******************************************************
			 * tryでparseLongでlong型に変換させていて
			 * 半角数字以外を入力したらエラー文を引っ張ってきて
			 * やり直させている
			 ***************************************************/
			try {
				result = Long.parseLong(in);
			} catch (NumberFormatException e) {
				Display.println(InputError.NumericCharacters.message);
				continue;
			}
			/*******************************************************
			 * 最少掛け金より少なかったらエラーを吐く様にしている
			 ***************************************************/
			if (chips.getMinBetValue() > result) {
				Display.println(InputError.MinimumBet.format(chips.getMinBetValue()));
			}
			/*******************************************************
			 * 最大掛け金より高かったらエラーを吐く様にしている
			 ***************************************************/
			else if (chips.getMaxBetValue() < result) {
				Display.println(InputError.MaxmumBet.format(chips.getMaxBetValue()));
			}
			/*******************************************************
			 * それでもなければループ終わり
			 ***************************************************/
			else {
				break;
			}
		}
		/*******************************************************
		 * 書いた数値resultをreturnで返している
		 ***************************************************/
		return result;
	}

	/**********************************************************
	 * Big or Small選択
	 * @param firstCard
	 * @return
	 * true: Big
	 * false: Small
	 **************************************************************/
	public boolean isBigOrSmall(Card firstCard) {
		Display.println(Prompt.BigOrSmallSelecter.format(firstCard.toString()));
		return isKeyIn(Prompt.BigOrSmall.message);
	}

	/**
	 * Big or Smallを続けるか選択
	 * @param bet
	 * @return
	 */
	public boolean isNextBet(long bet) {
		return isKeyIn(Prompt.NextBetting.format(bet));
	}

	/**
	 * ゲーム終了の選択
	 * @param chips
	 * @return
	 */
	public boolean isGameEnd(Chips chips) {
		if (0 >= chips.getTatal()) {
			Display.println(Prompt.NoChips.message);
			return false;
		}
		return isKeyIn(Prompt.GameEnd.message);
	}

	/********************************************
	 * Yes or No 選択の入力
	 * @param out プロンプトの文字列
	 * @return
	 * true: Yesが選択された
	 * false: Noが選択された
	 ***********************************************/
	private boolean isKeyIn(String out) {
		while (true) {
			if (!"".equals(out)) {
				Display.println(out);
			}
			switch (getKeyIn()) {
			case 0:
				return true;
			case 1:
				return false;
			}
		}
	}

	/**
	 * スキャナーからの数値を取得する
	 * @return
	 * 数値は０か１のみを入力できる。それ以外の数値、もしくは文字列は−１を返却する
	 */
	private int getKeyIn() {
		int result;
		String in = scanner.nextLine();
		if(in.equals("0")|| in.equals("1")){
				result = Integer.parseInt(in);
			return result;
		}else{
			Display.println(InputError.NumericZeroOrOwn.message);
			return -1;
		}
	}
}