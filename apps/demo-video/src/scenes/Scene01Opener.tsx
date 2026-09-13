import React from 'react';
import { interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { theme } from '../theme';

export const Scene01Opener: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const logoOpacity = interpolate(frame, [0, 25], [0, 1], { extrapolateRight: 'clamp' });
  const logoScale = spring({ frame, fps, config: { damping: 14 } });

  const textOpacity = interpolate(frame, [35, 65], [0, 1], { extrapolateRight: 'clamp' });
  const textTranslateY = interpolate(frame, [35, 65], [20, 0], { extrapolateRight: 'clamp' });

  return (
    <div
      style={{
        flex: 1,
        backgroundColor: theme.colors.bg,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        position: 'relative',
        padding: '0 120px',
        textAlign: 'center',
      }}
    >
      <div
        style={{
          opacity: logoOpacity,
          transform: `scale(${logoScale})`,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
      >
        <div
          style={{
            fontSize: '110px',
            fontFamily: theme.fonts.serif,
            fontWeight: 700,
            letterSpacing: '12px',
            color: theme.colors.accentLight,
            textShadow: '0 0 40px rgba(216, 155, 66, 0.4)',
            marginBottom: '4px',
          }}
        >
          F.R.E.D
        </div>
        <div
          style={{
            fontSize: '18px',
            fontFamily: theme.fonts.mono,
            color: theme.colors.textMuted,
            letterSpacing: '4px',
            textTransform: 'uppercase',
            marginBottom: '40px',
          }}
        >
          Project Sentinel · Real-Time SPEI Fraud Sentinel
        </div>
      </div>

      <div
        style={{
          opacity: textOpacity,
          transform: `translateY(${textTranslateY}px)`,
          maxWidth: '920px',
        }}
      >
        <p
          style={{
            fontSize: '34px',
            lineHeight: 1.45,
            color: theme.colors.textPrimary,
            fontFamily: theme.fonts.serif,
            fontWeight: 400,
            margin: 0,
          }}
        >
          Una API en tiempo real que mitiga el fraude por manipulación interceptando transferencias SPEI antes de su liquidación.
        </p>
      </div>
    </div>
  );
};
